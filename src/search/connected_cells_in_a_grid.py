#!/usr/bin/python3

# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

n = int(input().strip())
m = int(input().strip())
mat = []
for i in range(n):
    mat.append([int(i) for i in input().strip().split(" ")])

visited = [[0 for i in range(m)] for j in range(n)]
size = 0
max_size = 0


def is_valid(mat, i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m and mat[i][j] != 0


def neighbours(mat, i, j, n, m):
    nbrs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
            (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)]

    valid_nbrs = []
    for (i, j) in nbrs:
        if is_valid(mat, i, j, n, m):
            valid_nbrs.append((i, j))
    return valid_nbrs


def dfs(mat, i, j):
    visited[i][j] = True
    global size
    size += 1
    for (k, l) in neighbours(mat, i, j, n, m):
        if not visited[k][l]:
            dfs(mat, k, l)


for i in range(n):
    for j in range(m):
        size = 0
        if mat[i][j] == 1 and visited[i][j] == 0:
            dfs(mat, i, j)
            if size > max_size:
                max_size = size

print(max_size)
