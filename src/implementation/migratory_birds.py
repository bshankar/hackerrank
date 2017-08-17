#!/usr/bin/python3

# https://www.hackerrank.com/challenges/migratory-birds/problem


n = int(input().strip())
birds = [int(i) for i in input().strip().split(" ")]
count = [0, 0, 0, 0, 0, 0]

for i in birds:
    count[i] += 1

print(count.index(max(count)))
