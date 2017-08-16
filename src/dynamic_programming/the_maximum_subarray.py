#!/usr/bin/python3

# https://www.hackerrank.com/challenges/maxsubarray/problem


def max_subsequence(arr):
    result = sum(i for i in arr if i > 0)
    if result > 0:
        return result
    return max(arr)


def max_subarray(arr):
    best_so_far = -1e100
    best_including = -1e00

    for i in arr:
        best_including = max(i, best_including + i)
        best_so_far = max(best_including, best_so_far)
    return best_so_far


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    print(max_subarray(arr), end=" ")
    print(max_subsequence(arr))
