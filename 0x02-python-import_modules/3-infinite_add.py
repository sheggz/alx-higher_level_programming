#!/usr/bin/python3
import sys
sum = 0
for x in range(1, len(sys.argv)):
    sum = sum + int(sys.argv[x])
if __name__ == '__main__':
    print(sum)
