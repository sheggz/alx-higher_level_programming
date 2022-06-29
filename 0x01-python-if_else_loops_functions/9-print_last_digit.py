#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        unit = (number * -1) % 10
    else:
        unit = number % 10

    print('{:d}'.format(unit), end='')
    return unit
