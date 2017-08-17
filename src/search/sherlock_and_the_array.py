#!/usr/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-array/problem


def satisfies(arr):
    left_sum = 0
    right_sum = sum(arr[1:])
    for i in range(1, len(arr)):
        if left_sum == right_sum:
            return "YES"
        left_sum += arr[i - 1]
        right_sum -= arr[i]

    if left_sum == right_sum:
        return "YES"
    return "NO"


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    print(satisfies(arr))
