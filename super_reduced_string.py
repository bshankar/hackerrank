# https://www.hackerrank.com/challenges/reduced-string/problem


def super_reduced_string(s):
    s_list = list(s)

    is_reduced = True
    while is_reduced:
        i = 0
        is_reduced = False
        while i < len(s_list) - 1:
            if s_list[i] == s_list[i + 1]:
                del s_list[i]
                del s_list[i]
                is_reduced = True
            else:
                i += 1

    if s_list:
        return "".join(s_list)
    return "Empty String"


s = input().strip()
print(super_reduced_string(s))
