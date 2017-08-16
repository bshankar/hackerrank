#!/usr/bin/python3

# https://www.hackerrank.com/challenges/closest-numbers/problem


n = int(input().strip())
arr = sorted([int(i) for i in input().strip().split(" ")])
min_diff = 1e100

for i in range(n - 1):
    if arr[i + 1] - arr[i] < min_diff:
        min_diff = arr[i + 1] - arr[i]

for i in range(n - 1):
    if arr[i + 1] - arr[i] == min_diff:
        print(arr[i], end=" ")
        print(arr[i + 1], end=" ")
