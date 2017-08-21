#!/usr/bin/python3

# https://www.hackerrank.com/challenges/game-of-thrones/problem


def can_be_palindrome(s):
    odd_counts = 0
    for ch in set(s):
        if s.count(ch) % 2 != 0:
            odd_counts += 1
            if odd_counts > 1:
                return "NO"
    return "YES"


print(can_be_palindrome(input()))
