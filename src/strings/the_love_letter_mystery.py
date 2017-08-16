#!/usr/bin/python3

# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem


def the_love_letter_mystery(s):
    s_list = list(s)
    changes = 0
    for i in range(0, len(s) // 2):
        if s_list[i] != s_list[-i - 1]:
            changes += abs(ord(s_list[i]) - ord(s_list[-i - 1]))

    return changes


t = int(input().strip())
for i in range(t):
    print(the_love_letter_mystery(input().strip()))
