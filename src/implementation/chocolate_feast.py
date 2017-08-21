#!/usr/bin/python3

# https://www.hackerrank.com/challenges/chocolate-feast/problem

t = int(input().strip())
for i in range(t):
    n, c, m = (int(i) for i in input().strip().split(" "))
    chocolates = 0
    wrappers = 0

    chocolates += n // c
    wrappers = chocolates
    while wrappers >= m:
        chocolates += wrappers // m
        wrappers -= wrappers // m * (m - 1)

    print(chocolates)
