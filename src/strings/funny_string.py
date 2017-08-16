#!/usr/bin/python3

# https://www.hackerrank.com/challenges/funny-string/problem


def is_funny(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != \
           abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i])):
            return "Not Funny"

    return "Funny"


t = int(input().strip())
for i in range(t):
    print(is_funny(input().strip()))
