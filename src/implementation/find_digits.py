#!/usr/bin/python3

# https://www.hackerrank.com/challenges/find-digits/problem

t = int(input().strip())
for i in range(t):
    a = input().strip()
    ans = 0
    for d in a:
        if d != "0" and int(a) % int(d) == 0:
            ans += 1
    print(ans)
