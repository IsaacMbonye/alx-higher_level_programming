#!/usr/bin/python3
#Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

#Print all the letters except q and e
#You can only use one print function with string format
#You can only use one loop in your code

for letter in 'abcdefghijklmnopqrstuvwxyz':
    if( letter != 'e'  and letter != 'q'):
            print("{}".format(letter), end = '')

#print('{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}{15}{16}{17}{18}{19}{20}{21}{22}{23}{24}{25}{26}'.format(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, end = '')

