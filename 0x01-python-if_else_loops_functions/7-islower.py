#!/usr/bin/python3
def islower(c):
    # ord(c) returns the int value of c
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False
