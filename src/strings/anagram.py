#!/usr/bin/python3

# https://www.hackerrank.com/challenges/anagram/problem


def min_steps_to_anagram(s):
    if len(s) % 2 != 0:
        return -1

    s1 = list(sorted(s[:len(s) // 2]))
    s2 = list(sorted(s[len(s) // 2:]))
    for ch in s1:
        if not s2:
            return 0

        if ch in s2:
            s2.remove(ch)
    return len(s2)


t = int(input().strip())
for i in range(t):
    print(min_steps_to_anagram(input().strip()))
