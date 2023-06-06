#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            char = chr(ord(c) - 32)
        else:
            char = a
        print("{:s}".format(char), end="")
    print('')
