# BOJ 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys, collections
input = sys.stdin.readline

N = int(input())
nodes = {k: [] for k in range(1, N+1)}
for _ in range(N-1):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i)

visit_check = [0] * (N+1)
parents = [0] * (N+1)
queue = collections.deque([1])
while queue:
    p = queue.pop()
    for s in nodes[p]:
        if not visit_check[s]:
            queue.append(s)
            parents[s] = p
            visit_check[s] = 1

[print(parents[i]) for i in range(2, N+1)]
