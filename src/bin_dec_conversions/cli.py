import argparse
import sys

import questionary

from .core import binary_to_decimal, decimal_to_binary


def main():
    parser = argparse.ArgumentParser(prog="bin-dec-conversions")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-d",
        "--to-decimal",
        metavar="BINARY",
        type=str,
        help="Convert a binary number to decimal",
    )
    group.add_argument(
        "-b",
        "--to-binary",
        metavar="DECIMAL",
        type=int,
        help="Convert a decimal number to binary",
    )
    parser.add_argument(
        "-w",
        "--width",
        metavar="WIDTH",
        type=int,
        help="Minimum number of binary digits, zero-padded (only with --to-binary)",
    )

    args = parser.parse_args()

    if args.width is not None and args.to_binary is None:
        parser.error("Width goes only with --to-binary")
    elif args.to_decimal is not None:
        try:
            result = binary_to_decimal(args.to_decimal)
        except ValueError as e:
            parser.error(str(e))
        print(f"The decimal equivalent of {args.to_decimal} is: {result}")
    elif args.to_binary is not None:
        try:
            if args.width is not None:
                result = decimal_to_binary(args.to_binary, args.width)
            else:
                result = decimal_to_binary(args.to_binary)
        except ValueError as e:
            parser.error(str(e))
        print(f"The binary equivalent of {args.to_binary} is {result}")
    else:
        conversion = questionary.select(
            "Which conversion do you want to perform?",
            choices=["Binary to decimal", "Decimal to binary", "Exit"],
        ).ask()

        match conversion:
            case "Binary to decimal":
                while True:
                    try:
                        binary = input("Insert a binary number: ").strip()
                        print(
                            f"The decimal equivalent of {binary} is {binary_to_decimal(binary)}"
                        )
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                    else:
                        break
            case "Decimal to binary":
                while True:
                    try:
                        decimal = int(input("Insert a decimal number: ").strip())
                        width_input = input(
                            "Width in bits (leave empty for none): "
                        ).strip()
                        if width_input:
                            result = decimal_to_binary(decimal, int(width_input))
                        else:
                            result = decimal_to_binary(decimal)
                        print(f"The binary equivalent of {decimal} is {result}")
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                    else:
                        break
            case "Exit":
                sys.exit("Program terminated")


if __name__ == "__main__":
    main()
