#!/usr/bin/python3
#The ASCII value of the lowercase alphabet is from 97 to 122. And, the ASCII value of the uppercase alphabet is from 65 to 90.
#Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

import string

for letter in string.ascii_lowercase:
    print(string.ascii_lowercase.index(letter) + 97, end = ' ')

#print(ascii_alphabet, end ='')

