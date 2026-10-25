# bin-dec-conversions

Python package that performs conversions between decimal and binary numbers. It can be used as a library, from the command line, or through an interactive prompt.

## Features

- Convert binary strings to decimal integers and the other way around
- Optional zero-padding to a minimum width when producing binary output
- Clear, descriptive error messages for invalid input
- Command-line interface with flags, plus an interactive menu when run without arguments
- Fully tested with `pytest`, including a round-trip check for every value from 0 to 255

## Requirements

- Python 3.10 or newer
- [`questionary`](https://github.com/tmbo/questionary) (installed automatically, used for the interactive menu)

## Installation

```bash
pip install bin-dec-conversions
```

## Usage

### As a library

```python
from bin_dec_conversions import binary_to_decimal, decimal_to_binary

binary_to_decimal("1010")      # 10
decimal_to_binary(10)          # "1010"
decimal_to_binary(10, 8)       # "00001010"  (zero-padded to 8 digits)
decimal_to_binary(5, 2)        # "101"       (width is a minimum, never truncates)
```

| Function | Description |
| --- | --- |
| `binary_to_decimal(binary: str) -> int` | Converts a string of `0`s and `1`s to an integer. |
| `decimal_to_binary(decimal: int, width: int = 0) -> str` | Converts a non-negative integer to a binary string, left-padded with zeros to at least `width` digits. |

Both functions raise `ValueError` on invalid input:

- `binary_to_decimal` rejects empty strings and any character other than `0` and `1` (including spaces, signs, prefixes like `0b`, underscores and decimal points). The message lists every offending character.
- `decimal_to_binary` rejects negative numbers and negative widths.

```python
>>> binary_to_decimal("1a2")
ValueError: '1a2' is not a valid binary number: invalid character(s) '2', 'a'. Only 0 and 1 are allowed
```

### From the command line

```bash
# Binary to decimal
bin-dec-conversions -d 1010
# The decimal equivalent of 1010 is: 10

# Decimal to binary
bin-dec-conversions -b 10
# The binary equivalent of 10 is 1010

# Decimal to binary, zero-padded to 8 digits
bin-dec-conversions -b 10 -w 8
# The binary equivalent of 10 is 00001010
```

| Option | Description |
| --- | --- |
| `-d BINARY`, `--to-decimal BINARY` | Convert a binary number to decimal. |
| `-b DECIMAL`, `--to-binary DECIMAL` | Convert a decimal number to binary. |
| `-w WIDTH`, `--width WIDTH` | Minimum number of binary digits, zero-padded. Only valid together with `--to-binary`. |

`--to-decimal` and `--to-binary` are mutually exclusive.

### Interactive mode

Run the command with no arguments to open an interactive menu:

```bash
bin-dec-conversions
```

You can choose *Binary to decimal*, *Decimal to binary* (with an optional width), or *Exit*. Invalid input is reported and you are prompted again.

## Development

Clone the repository and install the package in editable mode with the development dependencies:

```bash
git clone https://github.com/JustM4rk123/bin-dec-conversions.git
cd bin-dec-conversions
pip install -e ".[dev]"
```

Run the tests and the linter:

```bash
pytest
ruff check .
```

## Project structure

```
src/bin_dec_conversions/
├── __init__.py   # public API and __version__
├── core.py       # conversion functions
└── cli.py        # command-line and interactive interface
tests/
├── test_conversions.py
└── test_invalid.py
```

## License

Released under the [MIT License](LICENSE).

Author: Marco S. Tornabene
