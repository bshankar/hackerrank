#!/usr/bin/python3

# https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input().strip())
s = input().strip()
h = 0
in_valley = 0
valleys = 0

for ch in s:
    if ch == "U":
        h += 1
    else:
        h -= 1

    if h < 0:
        in_valley = True
    elif h >= 0 and in_valley:
        in_valley = False
        valleys += 1

print(valleys)
