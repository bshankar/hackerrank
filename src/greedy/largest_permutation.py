#!/usr/bin/python3

# https://www.hackerrank.com/challenges/largest-permutation/problem


n, k = (int(i) for i in input().strip().split(" "))
arr = [int(i) for i in input().strip().split(" ")]

indices = [0 for i in range(n + 1)]
for i in range(n):
    indices[arr[i]] = i

i = 0
swaps = 0
while swaps < k and i < len(arr):
    if arr[i] != n - i:
        l = indices[n - i]
        arr[i], arr[indices[n - i]] = arr[indices[n - i]], arr[i]
        indices[arr[i]], indices[arr[l]] = indices[arr[l]], indices[arr[i]]
        swaps += 1
    i += 1

for i in arr:
    print(i, end=" ")
