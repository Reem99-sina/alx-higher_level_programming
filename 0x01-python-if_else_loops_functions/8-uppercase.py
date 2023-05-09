#!/usr/bin/python3
def uppercase(str):
    upperstring = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            upperstring += chr(ord(char) - 32)
        else:
            upperstring += char
    print("{}".format(upperstring))
