#!/usr/bin/python3

# https://www.hackerrank.com/challenges/the-time-in-words/problem

names = ["twelve", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
         "eighteen", "nineteen"]


def time(h, m):
    if m == 0:
        return names[h] + " o' clock"
    elif m == 15:
        return "quarter past " + names[h]
    elif m == 30:
        return "half past " + names[h]
    elif m == 45:
        return "quarter to " + names[(h + 1) % 12]
    elif m < 20:
        return names[m] + " minutes past " + names[h]
    elif m > 40:
        return names[60 - m] + " minutes to " + names[(h + 1) % 12]
    elif m < 30:
        return "twenty " + names[m % 10] + " minutes past " + names[h]
    return "twenty " + names[(60 - m) % 10] + \
        " minutes to " + names[(h + 1) % 12]


h = int(input().strip())
m = int(input().strip())
print(time(h, m))
