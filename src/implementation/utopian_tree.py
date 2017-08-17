#!/usr/bin/python3

# https://www.hackerrank.com/challenges/utopian-tree/problem


def get_height(n):
    h = 1
    for i in range(n):
        if i % 2 == 0:
            h *= 2
        else:
            h += 1
    return h


t = int(input().strip())
for i in range(t):
    print(get_height(int(input().strip())))
