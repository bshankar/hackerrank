#!/usr/bin/python3

# https://www.hackerrank.com/challenges/countingsort1/problem


n = int(input().strip())
count = {i: 0 for i in range(100)}
numbers = [int(i) for i in input().strip().split(" ")]
for i in range(n):
    count[numbers[i]] += 1

for i in range(100):
    print(count[i], end=" ")
