#!/usr/bin/python

import sys

def num_digits(n):
    if (n//10 == 0):
        return 1
    return 1 + num_digits(n//10)

def game_count(n):
    if (n <= 0):
        return 0
    count = 1
    while (n != 1):
        count += 1
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
    return count

def print_header(i, n):
    for k in range(num_digits(n) - num_digits(i)):
        print(' ', end = '')
    print(str(i) + ": ", end = '')


def print_hist(i, n, max_val):
    print_header(i, max_val)

    # I need this stupid case because of line wrapping
    if (n > 50):
        print(n)
        return
   
    for i in range(n):
        print('x', end = '')
    print(' --- ' + str(n))

def pattern(n):
    max_val = 0
    for i in range(n):
        pos = game_count(i)
        print_hist(i, pos, n - 1)
        if (pos > max_val):
            max_val = pos
    print("\n\n\n")
    print("max: " + str(max_val))



if (len(sys.argv) > 1):
    pattern(int(sys.argv[1]))
else:
    pattern(100)

