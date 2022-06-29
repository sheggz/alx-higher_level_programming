#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        str = ''
        if n % 3 == 0:
            str += 'Fizz'
        if n % 5 == 0:
            str += 'Buzz'
        if len(str) == 0:
            print(f'{n}', end=' ')
        else:
            print(f'{str}', end=' ')
