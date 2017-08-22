#!/usr/bin/python3

# https://www.hackerrank.com/challenges/jim-and-the-orders/problem
import operator

n = int(input().strip())
f = {}

for i in range(n):
    ti, di = (int(i) for i in input().strip().split(" "))
    f[i] = ti + di

f_sorted = sorted(f.items(), key=operator.itemgetter(1))
for i in f_sorted:
    print(i[0] + 1, end=" ")
