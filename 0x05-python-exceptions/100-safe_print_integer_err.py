#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    # since we're using :d format specifier it should throw an error
    # if its not an integer
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print("Exception: {:s}".format(str(ve)), file=sys.stderr)
        return False
    except TypeError as te:
        print("Exception".format(str(te)), file=sys.stderr)
        return false
