#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print("{:c}".format(ord(char) + (ord('a') - ord('A'))), end='')
