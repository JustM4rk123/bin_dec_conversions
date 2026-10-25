import re

import pytest

from bin_dec_conversions import binary_to_decimal, decimal_to_binary


@pytest.mark.parametrize(
    "invalid, expected_in_message",
    [
        ("", "empty"),
        ("2", "character(s) '2'"),
        ("10_1", "'_'"),
        ("-101", "'-'"),
        ("0b101", "'b'"),
        (" 101", "' '"),
        ("1.0", "'.'"),
    ],
)
def test_bin2dec_error_messages(invalid, expected_in_message):
    with pytest.raises(ValueError, match=re.escape(expected_in_message)):
        binary_to_decimal(invalid)


def test_bin2dec_message_echoes_input():
    with pytest.raises(ValueError, match=re.escape("'10_1'")):
        binary_to_decimal("10_1")


def test_bin2dec_message_lists_every_invalid_char():
    with pytest.raises(ValueError) as exc:
        binary_to_decimal("1a2b")
    assert "'a'" in str(exc.value)
    assert "'2'" in str(exc.value)
    assert "'b'" in str(exc.value)


def test_dec2bin_negative_number_message():
    with pytest.raises(ValueError, match="negative"):
        decimal_to_binary(-5)


def test_dec2bin_negative_width_message():
    with pytest.raises(ValueError, match="Width cannot be negative"):
        decimal_to_binary(5, -1)
