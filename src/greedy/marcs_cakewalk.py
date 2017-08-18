#!/usr/bin/python3

# https://www.hackerrank.com/challenges/marcs-cakewalk/problem


n = int(input().strip())
C = sorted([int(i) for i in input().strip().split(" ")], reverse=True)

sum_ = 0
for i in range(len(C)):
    sum_ += 2**i * C[i]

print(sum_)
