#!/usr/bin/python3
#Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

#Print all the letters except q and e
#You can only use one print function with string format
#You can only use one loop in your code

import string

for letter in string.ascii_lowercase:
    if (string.ascii_lowercase.index(letter) + 97) == 101:
      string.ascii_lowercase.replace(letter, '')
    elif (string.ascii_lowercase.index(letter) + 97) == 113:
      string.ascii_lowercase.replace(letter, '')

    else:
        print(string.ascii_lowercase.index(letter) + 97, end = ' ')

