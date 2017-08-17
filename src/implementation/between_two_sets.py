#!/usr/bin/python3

# https://www.hackerrank.com/challenges/between-two-sets/problem

n, m = (int(i) for i in input().strip().split(" "))
A = [int(i) for i in input().strip().split(" ")]
B = [int(i) for i in input().strip().split(" ")]

factors_of_B = set()

for x in range(1, 101):
    # x is a factor of all elements in B
    is_factor = True
    for b in B:
        if b % x != 0:
            is_factor = False
            break
    if is_factor:
        factors_of_B.add(x)

# all elements in A are factors of x
result = len(factors_of_B)
for x in factors_of_B:
    for a in A:
        if x % a != 0:
            result -= 1
            break

print(result)
