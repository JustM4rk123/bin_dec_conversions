import pytest

from bin_dec_conversions import binary_to_decimal, decimal_to_binary


@pytest.mark.parametrize(
    "binary, expected",
    [
        ("0", 0),
        ("1010", 10),
        ("101", 5),
        ("10000000", 128),
    ],
)
def test_bin2dec(binary, expected):
    assert binary_to_decimal(binary) == expected


@pytest.mark.parametrize(
    "decimal, expected",
    [
        (0, "0"),
        (10, "1010"),
        (5, "101"),
        (128, "10000000"),
    ],
)
def test_dec2bin(decimal, expected):
    assert decimal_to_binary(decimal) == expected


def test_dec2bin_padding():
    assert decimal_to_binary(10, 8) == "00001010"
    assert decimal_to_binary(0, 8) == "00000000"
    assert decimal_to_binary(5, 2) == "101"


@pytest.mark.parametrize("n", range(256))
def test_round_trip(n):
    assert binary_to_decimal(decimal_to_binary(n)) == n
