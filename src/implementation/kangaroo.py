#!/usr/bin/python3

# https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroos_meet(x1, v1, x2, v2):
    if v1 == v2 and x1 != x2:
        return "NO"
    elif (x1 - x2) % (v2 - v1) == 0:
        t = (x1 - x2) / (v2 - v1)
        if t > 0:
            return "YES"
    return "NO"


x1, v1, x2, v2 = (int(i) for i in input().strip().split(" "))
print(kangaroos_meet(x1, v1, x2, v2))
