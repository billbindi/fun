#!/usr/bin/python

import sys
from printer import my_print

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
        my_print(' ', e = '')
    my_print(str(i) + ": ", e = '')


def print_hist(i, n, max_val):
    print_header(i, max_val)

    # I need this stupid case because of line wrapping
    if (n > 50):
        my_print(n)
        return
   
    for i in range(n):
        my_print('x', e = '')
    my_print(' -- ' + str(n))

def pattern(n):
    max_val = 0
    for i in range(n):
        pos = game_count(i)
        print_hist(i, pos, n - 1)
        if (pos > max_val):
            max_val = pos
    my_print('')
    my_print("max: " + str(max_val))

def game_build(n):
    if (n <= 0):
        return False
    lis = []
    while (n != 1):
        lis.append(int(n))
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
    lis.append(1)
    return lis

def game(n):
    lis = game_build(n)
    steps = len(lis)
    for i in range(steps):
        print_header(i + 1, steps)
        my_print(lis[i])


def print_usage():
    my_print("Usage for the 3n + 1 game")
    my_print("         python <file> <type> <num>\n")
    my_print("         file - {game.py | game27.py}, game.py for python versions 3 and above, else game27.py")
    my_print("         type - {freq | one}, frequency will show hitogram data of the number of steps taken for 1 - num, one will just run it once and show the steps needed for num")
    my_print("         num  - either the max value for frequency mode or the value to display for one mode")


if (len(sys.argv) <= 2):
    print_usage()
else:
    ops = sys.argv[1:]
    if (ops[0] == "freq"):
        pattern(int(ops[1]))
    elif (ops[0] == "one"):
        game(int(ops[1]))
    else:
        print_usage()
