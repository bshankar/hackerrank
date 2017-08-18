#!/usr/bin/python3

# https://www.hackerrank.com/challenges/angry-children/problem


n = int(input().strip())
k = int(input().strip())
arr = []
for i in range(n):
    arr.append(int(input().strip()))

arr.sort()
i = 0
j = k - 1
min_ = 1000000000

while j < len(arr):
    unfairness = arr[j] - arr[i]
    if unfairness < min_:
        min_ = unfairness
    i += 1
    j += 1

print(min_)
