#!/usr/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem


def decent_number(n):
    for i in range(n // 3 * 3, -1, -3):
        if (n - i) % 5 == 0:
            return "5" * i + "3" * (n - i)
    return -1


t = int(input().strip())
for i in range(t):
    print(decent_number(int(input().strip())))
