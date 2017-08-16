#!/usr/bin/python3

# https://www.hackerrank.com/challenges/bigger-is-greater/problem


def next_permutation(s):
    s_list = list(s)
    i = len(s_list) - 1
    while i > 0 and s_list[i - 1] >= s_list[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    j = len(s_list) - 1
    while s_list[j] <= s_list[i - 1]:
        j -= 1

    s_list[i - 1], s_list[j] = s_list[j], s_list[i - 1]
    s_list[i:] = s_list[len(s_list) - 1: i - 1: -1]
    return "".join(s_list)


t = int(input().strip())
for i in range(t):
    print(next_permutation(input().strip()))
