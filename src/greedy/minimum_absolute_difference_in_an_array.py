#!/usr/bin/python3

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem


n = int(input().strip())
arr = sorted([int(i) for i in input().strip().split(" ")])
min_ = 1000000000

for i in range(n - 1):
    if arr[i + 1] - arr[i] < min_:
        min_ = arr[i + 1] - arr[i]

print(min_)
