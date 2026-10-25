from importlib.metadata import PackageNotFoundError, version

from .core import binary_to_decimal, decimal_to_binary

try:
    __version__ = version("bin-dec-conversions")
except PackageNotFoundError:  # running from source without installing
    __version__ = "unknown"

__all__ = ["__version__", "binary_to_decimal", "decimal_to_binary"]
