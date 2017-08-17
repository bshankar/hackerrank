#!/usr/bin/python3

# https://www.hackerrank.com/challenges/equality-in-a-array/problem


n = int(input().strip())
arr = [int(i) for i in input().strip().split(" ")]
counts = [0 for i in range(101)]
max_count = 0
for i in arr:
    counts[i] += 1
    if counts[i] > max_count:
        max_count = counts[i]
print(n - max_count)
