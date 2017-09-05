#!/usr/bin/python3

# https://www.hackerrank.com/challenges/fair-rations/problem

n = int(input().strip())
arr = [(int(i) + 1) % 2 for i in input().strip().split(" ")]
distributed = 0

for i in range(len(arr) - 1):
    if arr[i] == 0:
        arr[i] ^= 1
        arr[i + 1] ^= 1
        distributed += 2

if arr[-1]:
    print(distributed)
else:
    print("NO")
