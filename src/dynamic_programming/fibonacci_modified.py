#!/usr/bin/python3

# https://www.hackerrank.com/challenges/fibonacci-modified/problem


def fib_mod(t1, t2, n):
    if n == 1:
        return t1
    if n == 2:
        return t2

    for i in range(n - 2):
        t1, t2 = t2, t1 + t2**2

    return t2


t1, t2, n = (int(i) for i in input().strip().split(" "))
print(fib_mod(t1, t2, n))
