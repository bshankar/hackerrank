#!/usr/bin/python3

# https://www.hackerrank.com/challenges/manasa-and-stones/problem

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    last_stones = set()

    for j in range(n):
        last_stones.add(j * a + (n - j - 1) * b)

    for stone in sorted(last_stones):
        print(stone, end=" ")
    print()
