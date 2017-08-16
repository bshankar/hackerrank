#!/usr/bin/python3

# https://www.hackerrank.com/challenges/two-strings/problem


def have_common_substr(s1, s2):
    return len(set(s1).intersection(set(s2))) != 0


t = int(input().strip())
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    if have_common_substr(s1, s2):
        print("YES")
    else:
        print("NO")
