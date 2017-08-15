#!/usr/bin/python3

# https://www.hackerrank.com/challenges/pangrams/problem


def is_pangram(s):
    s = s.lower()
    if len(set(s)) == 27:
        return "pangram"
    return "not pangram"


print(is_pangram(input().strip()))
