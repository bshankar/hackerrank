#!/usr/bin/python3

# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

t = int(input().strip())
for i in range(t):
    x, y, z = (int(i) for i in input().strip().split(" "))
    if abs(x - z) > abs(y - z):
        print("Cat B")
    elif abs(x - z) < abs(y - z):
        print("Cat A")
    else:
        print("Mouse C")
