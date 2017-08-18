#!/usr/bin/python3

# https://www.hackerrank.com/challenges/bfsshortreach/problem

import queue


class Graph:
    """Undirected, unweighted graph"""

    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.graph = [[] for i in range(n)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, root):
        s = set()
        q = queue.Queue(self.v)
        dist = [-1 for i in range(self.v)]
        dist[root] = 0

        s.add(root)
        q.put(root)

        while not q.empty():
            u = q.get()

            for v in self.graph[u]:
                if v not in s:
                    s.add(v)
                    q.put(v)
                    dist[v] = dist[u] + 1
        return dist


q = int(input().strip())
for i in range(q):
    n, m = (int(i) for i in input().strip().split(" "))
    g = Graph(n, m)
    for j in range(m):
        u, v = (int(i) for i in input().strip().split(" "))
        g.add_edge(u - 1, v - 1)
    s = int(input().strip()) - 1

    for d in g.bfs(s):
        if d > 0:
            print(6 * d, end=" ")
        elif d == -1:
            print(d, end=" ")
    print()
