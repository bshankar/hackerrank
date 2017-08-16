#!/usr/bin/python3

# https://www.hackerrank.com/challenges/big-sorting/problem

a = []
n = int(input().strip())
for i in range(n):
    a.append(input().strip())

for i in sorted(a, key=int):
    print(i)
