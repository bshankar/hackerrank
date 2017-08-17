#!/usr/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

from math import sqrt, floor, ceil


def squares_between(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1


t = int(input().strip())
for i in range(t):
    a, b = (int(i) for i in input().strip().split(" "))
    print(squares_between(a, b))
