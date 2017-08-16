#!/usr/bin/python3

# https://www.hackerrank.com/challenges/gem-stones/problem


n = int(input().strip())
s = set([chr(i) for i in range(ord("a"), ord("z") + 1)])
for i in range(n):
    s = s.intersection(set(input().strip()))

print(len(s))
