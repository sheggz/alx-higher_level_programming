#!/usr/bin/python3

def safe_print_integer(value):
    # since we're using :d format specifier it should throw an error
    # if its not an integer
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
