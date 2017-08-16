#!/usr/bin/python3

# https://www.hackerrank.com/challenges/countingsort2/problem


n = int(input().strip())
count = [0 for i in range(100)]
numbers = [int(i) for i in input().strip().split(" ")]
for i in range(n):
    count[numbers[i]] += 1

for i in range(100):
    for j in range(count[i]):
        print(i, end=" ")
