#!/usr/bin/python3

# https://www.hackerrank.com/challenges/repeated-string/problem


def repeats_within(s, n):
    locs = [i for i in range(len(s)) if s[i] == "a"]
    result = n // len(s) * len(locs)
    remaining_len = n % len(s)
    for i in locs:
        if i < remaining_len:
            result += 1

    return result


s = input().strip()
n = int(input().strip())
print(repeats_within(s, n))
