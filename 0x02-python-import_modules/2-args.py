#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv) - 1
    plural = 's' if count != 1 else ''
    sign = ':' if count > 0 else '.'
    print('{} argument{}{}'.format(count, plural, sign))
    for i in range(1, count + 1):
        print('{}: {}'.format(i, sys.argv[i]))
