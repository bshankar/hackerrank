#!/usr/bin/python3

# https://www.hackerrank.com/challenges/cut-the-sticks/problem

n = int(input().strip())
sticks = sorted([int(i) for i in input().strip().split(" ")])

while sticks:
    print(len(sticks))
    min_ = sticks[0]
    sticks = [i - min_ for i in sticks if i - min_ > 0]
