#!/usr/bin/python3
# a function that removes all characters c and C from a string

def no_c(my_string):
    word = [x for x in my_string]
    for i in word:
        if i == 'c' or i == 'C':
            word[word.index(i)] = ""
    return ("".join(word))
