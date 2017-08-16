#!/usr/bin/python3

# https://www.hackerrank.com/challenges/beautiful-binary-string/problem


def min_steps(s):
    changes = 0
    while s.find("010") != -1:
        s = s.replace("010", "011", 1)
        changes += 1
    return changes


size = input().strip()
s = input().strip()
print(min_steps(s))
