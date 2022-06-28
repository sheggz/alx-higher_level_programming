#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = -1*((-1 * number) % 10)
else:
    last_num = number % 10

if last_num > 5:
    strr = "and is greater than 5"
elif last_num == 0:
    strr = "and is 0"
elif last_num < 6 and last_num != 0:
    strr = "and is less than 6 and not 0"
print(f"last digit of {number} is {last_num} {strr}\n")
