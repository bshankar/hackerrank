#!/usr/bin/python3

# https://www.hackerrank.com/challenges/greedy-florist/problem

n, k = (int(i) for i in input().strip().split(" "))
C = sorted([int(i) for i in input().strip().split(" ")], reverse=True)

cost = 0
x = 0
j = 0

while j < n:
    for i in range(k):
        if j >= n:
            break
        cost += (x + 1) * C[j]
        j += 1
    x += 1

print(cost)
