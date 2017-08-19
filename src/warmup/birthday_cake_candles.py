#!/usr/bin/python3

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

n = int(input().strip())
arr = [int(i) for i in input().strip().split(" ")]
print(arr.count(max(arr)))
