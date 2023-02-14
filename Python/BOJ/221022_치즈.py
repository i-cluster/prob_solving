# BOJ 2636 치즈
# https://www.acmicpc.net/problem/2636

import sys
from collections import Counter, deque
s_input = sys.stdin.readline

N, M = map(int, s_input().split())
board = list(s_input().split() for _ in range(N))
last_chz = sum(Counter(board[i])['1'] for i in range(N))
cnt = 0

d = [0, 1, 0, -1, 0]
que = deque([(0, 0)])
# 공기 0, 치즈 1, 탐색한 공기(외부 공기) 2, 탐색한 치즈 3
while last_chz:
    xy = deque()
    while que:
        x, y = que.popleft()
        for k in range(4):
            dx, dy = x + d[k], y + d[k+1]
            if 0 <= dx < N and 0 <= dy < M:
                if board[dx][dy] == '0': que.append((dx, dy))
                elif board[dx][dy] == '1': xy.append((dx, dy))
                board[dx][dy] = ''

    last_chz -= len(xy)
    que = xy
    cnt += 1

print(cnt)
print(len(xy))
