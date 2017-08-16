# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem


def is_hackerrank_subsequence(s):
    i, j = 0, 0
    target = "hackerrank"
    while i < len(s) and j < len(target):
        if s[i] == target[j]:
            j += 1
        i += 1
    if j == len(target):
        return "YES"
    return "NO"


t = int(input().strip())
for i in range(t):
    print(is_hackerrank_subsequence(input().strip()))
