#!/usr/bin/python3

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

heights = [int(i) for i in input().strip().split(" ")]
s = input().strip()
print(len(s) * max([heights[ord(ch) - ord("a")] for ch in s]))
