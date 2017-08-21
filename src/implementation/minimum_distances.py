#!/usr/bin/python3

# https://www.hackerrank.com/challenges/minimum-distances/problem

n = int(input().strip())
arr = [int(i) for i in input().strip().split(" ")]

indices = {}
for i in range(len(arr)):
    if arr[i] in indices:
        indices[arr[i]].append(i)
    else:
        indices[arr[i]] = [i]

min_dist = 1000000000
for val in indices:
    if len(indices[val]) > 1:
        for i in range(len(indices[val]) - 1):
            if min_dist > indices[val][i + 1] - indices[val][i]:
                min_dist = indices[val][i + 1] - indices[val][i]

if min_dist == 1000000000:
    min_dist = -1

print(min_dist)
