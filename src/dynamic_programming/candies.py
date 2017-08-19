#!/usr/bin/python3

# https://www.hackerrank.com/challenges/candies/problem


n = int(input().strip())
arr = []
for i in range(n):
    arr.append(int(input().strip()))

candies = [1 for i in range(n)]

for i in range(0, n - 1):
    if arr[i] < arr[i + 1]:
        candies[i + 1] = candies[i] + 1

for i in range(-1, -n, -1):
    if arr[i] < arr[i - 1] and candies[i] >= candies[i - 1]:
        candies[i - 1] = candies[i] + 1

print(sum(candies))
