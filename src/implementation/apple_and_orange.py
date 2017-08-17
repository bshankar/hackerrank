#!/usr/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

s, t = (int(i) for i in input().strip().split(" "))
a, b = (int(i) for i in input().strip().split(" "))
m, n = (int(i) for i in input().strip().split(" "))
apple = [int(i) for i in input().strip().split(" ")]
orange = [int(i) for i in input().strip().split(" ")]

print(len([d for d in apple if d >= s - a and d <= t - a]))
print(len([d for d in orange if d >= s - b and d <= t - b]))
