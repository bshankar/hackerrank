#!/usr/bin/python3

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


n = int(input().strip())
arr = [int(i) for i in input().strip().split(" ")]

min_record = arr[0]
min_record_broken = 0
max_record = arr[0]
max_record_broken = 0

for i in range(1, len(arr)):
    if arr[i] > max_record:
        max_record_broken += 1
        max_record = arr[i]
    if arr[i] < min_record:
        min_record_broken += 1
        min_record = arr[i]

print(max_record_broken, end=" ")
print(min_record_broken)
