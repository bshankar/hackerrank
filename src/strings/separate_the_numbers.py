#!/usr/bin/python3

# https://www.hackerrank.com/challenges/separate-the-numbers/problem


def is_beautiful(s):
    s_start = s
    for size in range(1, len(s) // 2 + 1):
        s = s_start
        n = int(s[:size])
        s = s[size:]
        n_start = n

        while s.find(str(n + 1)) == 0:
            size = len(str(n + 1))
            n = int(s[:size])
            s = s[size:]

        if not s:
            return "YES " + str(n_start)
    return "NO"


t = int(input().strip())
for i in range(t):
    print(is_beautiful(input().strip()))
