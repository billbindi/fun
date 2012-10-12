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
        print '',
    print str(i) + ": ",


def print_hist(i, n, max_val):
    print_header(i, max_val)

    # I need this stupid case because of line wrapping
    if (n > 50):
        print n
        return
   
    for i in range(n):
        print 'x',
    print ''

def pattern(n):
    for i in range(n):
        print_hist(i, game_count(i), n - 1)



if (len(sys.argv) > 1):
    pattern(int(sys.argv[1]))
else:
    pattern(100)
