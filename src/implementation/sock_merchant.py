#!/usr/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem

n = int(input().strip())
C = (int(i) for i in input().strip().split(" "))
count = [0 for i in range(101)]

for c in C:
    count[c] += 1

print(sum(i // 2 for i in count))
