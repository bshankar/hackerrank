#!/usr/bin/python3

# https://www.hackerrank.com/challenges/maximizing-xor/problem

from math import floor, log2

l = int(input().strip())
r = int(input().strip())
print(2**(floor(log2(l ^ r)) + 1) - 1)
