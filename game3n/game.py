#!/usr/bin/python

from sys import argv
from printer import my_print

def num_digits(n):
    if (n//10 == 0):
        return 1
    return 1 + num_digits(n//10)

def is_even(n):
    return not int(n) & 1

def game_build(n):
    lis = []
    if (n <= 0):
        return lis
    while (n != 1):
        lis.append(int(n))
        if (is_even(n)):
            n /= 2
        else:
            n = 3*n + 1
    lis.append(1)
    return lis

def print_header(i, n):
    for k in range(num_digits(n) - num_digits(i)):
        my_print(' ', e = '')
    my_print(str(i) + ": ", e = '')


def print_hist(i, n, max_val):
    print_header(i, max_val)

    # I need this stupid case because of line wrapping
    if (n > 150):
        my_print(n)
        return
   
    for k in range(n):
        my_print('x', e = '')
    if (i > 0):
        my_print(' -- ' + str(n))
    else:
    	my_print('0')

def pattern(n):
    max_val = 0
    for i in range(n):
        pos = len(game_build(i))
        print_hist(i, pos, n - 1)
        if (pos > max_val):
            max_val = pos
    my_print('')
    my_print("max: " + str(max_val))

def game(n):
    lis = game_build(n)
    steps = len(lis)
    if (steps > 0):
        for i in range(steps):
            print_header(i + 1, steps)
            my_print(lis[i])


def print_usage():
    my_print("Usage for the 3n + 1 game")
    my_print("         python game.py <type> <num>\n")
    my_print("         type - {freq | one}, frequency will show hitogram data of the number of steps taken for 1 - num, one will just run it once and show the steps needed for num")
    my_print("         num  - either the max value for frequency mode or the value to display for one mode")


if (len(argv) <= 2):
    print_usage()
else:
    ops = argv[1:]
    if (ops[0] == "freq"):
        pattern(int(ops[1]))
    elif (ops[0] == "one"):
        game(int(ops[1]))
    else:
        print_usage()
