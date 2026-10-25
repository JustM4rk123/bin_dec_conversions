def binary_to_decimal(binary: str) -> int:
    if not binary:
        raise ValueError("The input is empty. Enter a binary number made of 0s and 1s")

    invalid = sorted(set(binary) - {"0", "1"})
    if invalid:
        chars = ", ".join(repr(c) for c in invalid)
        raise ValueError(
            f"'{binary}' is not a valid binary number: "
            f"invalid character(s) {chars}. Only 0 and 1 are allowed"
        )

    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        if bit == "1":
            decimal += 2**i
    return decimal


def decimal_to_binary(decimal: int, width: int = 0) -> str:
    if decimal < 0:
        raise ValueError(
            f"{decimal} is negative. Only non-negative integers are supported"
        )
    if width < 0:
        raise ValueError(f"Width cannot be negative (got {width})")
    if decimal == 0:
        return "0".zfill(width)

    bits = []
    while decimal > 0:
        bits.append(str(decimal % 2))
        decimal //= 2
    return "".join(reversed(bits)).zfill(width)
