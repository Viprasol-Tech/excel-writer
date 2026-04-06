"""
excel-writer - Write data to Excel with formatting

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ExcelWriter, write, process, main

__all__ = ["ExcelWriter", "write", "process", "main"]
