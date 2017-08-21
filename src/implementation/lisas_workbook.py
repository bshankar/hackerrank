#!/usr/bin/python3

# https://www.hackerrank.com/challenges/lisa-workbook/problem

from math import ceil

n, k = (int(i) for i in input().strip().split(" "))
t = [int(i) for i in input().strip().split(" ")]
page = 1
count = 0

for ch in range(len(t)):
    for p in range(1, t[ch] + 1):
        if page == p:
            count += 1
        if p % k == 0 or t[ch] == p:
            page += 1

print(count)
