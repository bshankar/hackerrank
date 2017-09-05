#!/usr/bin/python3

# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

i, j, k = (int(i) for i in input().strip().split(" "))
ans = 0

for n in range(i, j + 1):
    if abs(n - int(str(n)[::-1])) % k == 0:
        ans += 1

print(ans)
