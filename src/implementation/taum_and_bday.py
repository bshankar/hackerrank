#!/usr/bin/python3

# https://www.hackerrank.com/challenges/taum-and-bday/problem

t = int(input().strip())
for i in range(t):
    b, w = (int(i) for i in input().strip().split(" "))
    x, y, z = (int(i) for i in input().strip().split(" "))
    print(b * min(x, y + z) + w * min(y, x + z))
