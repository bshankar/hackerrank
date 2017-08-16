#!/usr/bin/python3

# https://www.hackerrank.com/challenges/mark-and-toys/problem

n, k = (int(i) for i in input().strip().split(" "))
prices = sorted([int(i) for i in input().strip().split(" ")])
toys = 0
cost = 0

for i in prices:
    if i + cost <= k:
        cost += i
        toys += 1
    else:
        break

print(toys)
