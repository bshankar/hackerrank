#!/usr/bin/python3

# https://www.hackerrank.com/challenges/grading/problem


def next_five_multiple(n):
    if n % 10 <= 5:
        return n // 10 * 10 + 5
    return n // 10 * 10 + 10


def grade(n):
    if n >= 38 and next_five_multiple(n) - n < 3:
        return next_five_multiple(n)
    return n


n = int(input().strip())
for i in range(n):
    print(grade(int(input().strip())))
