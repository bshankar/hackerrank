#!/usr/bin/python3

# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

from math import ceil


def to_int(s):
    if s == "":
        return 0
    return int(s)


def is_modified_kaprekar(n):
    n2 = str(n**2)
    fh = len(n2) // 2
    return to_int(n2[fh:]) + to_int(n2[:fh]) == n


found = False
a = int(input().strip())
b = int(input().strip())
for i in range(a, b + 1):
    if is_modified_kaprekar(i):
        found = True
        print(i, end=" ")
if not found:
    print("INVALID RANGE")
