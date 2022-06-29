#!/usr/bin/python3
def uppercase(str):
    for char in str:
        offset = 0
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            offset = ord('A') - ord('a')
        print("{:c}".format(ord(char) + offset), end='')
    print()


