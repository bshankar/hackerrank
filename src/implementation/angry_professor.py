#!/usr/bin/python3

# https://www.hackerrank.com/challenges/angry-professor/problem

t = int(input().strip())
for i in range(t):
    n, k = (int(i) for i in input().strip().split(" "))
    on_time = sum([1 for i in input().strip().split(" ") if int(i) <= 0])
    if on_time >= k:
        print("NO")
    else:
        print("YES")
