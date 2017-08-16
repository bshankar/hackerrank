#!/usr/bin/python3

# https://www.hackerrank.com/challenges/find-the-median/problem


n = int(input().strip())
arr = sorted([int(i) for i in input().strip().split(" ")])
print(arr[n // 2])
