#!/usr/bin/python3

# https://www.hackerrank.com/challenges/two-arrays/problem

t = int(input().strip())
for i in range(t):
    n, k = (int(i) for i in input().strip().split(" "))
    A = sorted([int(i) for i in input().strip().split(" ")], reverse=True)
    B = sorted([int(i) for i in input().strip().split(" ")])

    satisfies = True
    for i in range(n):
        if A[i] + B[i] < k:
            print("NO")
            satisfies = False
            break

    if satisfies:
        print("YES")
