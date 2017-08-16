#!/usr/bin/python3

# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


n, k = (int(i) for i in input().strip().split(" "))
arr = [int(i) for i in input().strip().split(" ")]
pairs = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] + arr[j]) % k == 0:
            pairs += 1

print(pairs)
