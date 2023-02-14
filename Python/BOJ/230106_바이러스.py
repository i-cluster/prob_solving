# BOJ 2606 바이러스
# https://www.acmicpc.net/problem/2606

import sys
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

n = int(input()) + 1
com, visit = [set() for _ in range(n)], [0] * n
for _ in range(int(input())):
    i, j = map(int, input().split())
    com[i].add(j); com[j].add(i)

visit[1], check = 1, set(com[1])
while check:
    k = check.pop()
    if not visit[k]:
        visit[k] = 1
        [check.add(p) for p in com[k]]

print(visit.count(1) - 1)
