# https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()

i = 0
changed = 0
while i < len(s):
    if s[i] != "S":
        changed += 1
    if s[i + 1] != "O":
        changed += 1
    if s[i + 2] != "S":
        changed += 1

    i += 3

print(changed)
