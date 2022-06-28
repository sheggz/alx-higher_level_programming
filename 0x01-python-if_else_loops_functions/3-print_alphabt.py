#!/usr/bin/python3
for x in range(97, 123):
    if x == 101 or x == 113:
        continue
    print("{:c}".format(x), end='')
# chr(i) returns the string representing a character whose ascii value is i
# end = '' changes the default '\n' which ends the print statement to nothing
