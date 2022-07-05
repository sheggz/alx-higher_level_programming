#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = None
    if len(sentence) > 0:
        first_letter = sentence[0]
    # to return multiple thing we use a sequence: list ot tuple would do
    return [len(sentence), first_letter]
