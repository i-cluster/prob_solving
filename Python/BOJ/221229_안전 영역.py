# BOJ 2468 안전 영역
# https://www.acmicpc.net/problem/2468

def find_safe(x, y, h):
    d = [0, 1, 0, -1, 0]
    queue = deque([(x, y)])
    while queue:
        i, j = queue.pop()
        visits[i][j] = 1
        for k in range(4):
            di, dj = i + d[k], j + d[k+1]
            if area[di][dj] > h and visits[di][dj] == 0:
                queue.append((di, dj))


def flood(h):
    fields = 0
    for x in range(1, N+1):
        for y in range(1, N+1):
            if area[x][y] > h and visits[x][y] == 0:
                find_safe(x, y, h)
                fields += 1

    return fields


import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

N = int(input())
area = [[0] * (N+2)]

chk_set = set()
for k in range(1, N+1):
    arr = [0] + list(map(int, input().split())) + [0]
    [chk_set.add(i) for i in arr]
    area.append(arr)

area.append([0] * (N+2))

safe_fields = 0
for h in chk_set:
    visits = list([0] * (N+2) for _ in range(N+2))
    safe_fields = max(safe_fields, flood(h))

print(safe_fields)
