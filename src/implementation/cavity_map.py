#!/usr/bin/python3

# https://www.hackerrank.com/challenges/cavity-map/problem
import copy

n = int(input().strip())
arr = []
for i in range(n):
    arr.append([int(i) for i in input().strip()])

cavities = copy.deepcopy(arr)

for r in range(1, n - 1):
    for c in range(1, n - 1):
        d = arr[r][c]
        if d > arr[r - 1][c] and d > arr[r + 1][c] and \
                d > arr[r][c - 1] and d > arr[r][c + 1]:
            cavities[r][c] = "X"

for i in range(n):
    for j in range(n):
        print(cavities[i][j], end="")
    print()
