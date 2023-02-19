# BOJ 7562 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    I = int(input())
    i, j = map(int, input().split())
    ti, tj = map(int, input().split())

    board = [['X'] * (I+4)] * 2 + list(['X', 'X'] + [''] * I + ['X', 'X'] for _ in range(I)) + [['X'] * (I+4)] * 2
    board[ti+2][tj+2] = 'O'

    d = [1, 2, 1, -2, -1, 2, -1, -2, 1, -2]
    queue, temp_queue = deque([(i+2, j+2)]), deque([])

    if board[i+2][j+2] == 'O': moving_count = 0
    else:
        moving_count = 1
        while queue:
            x, y = queue.popleft()

            for k in range(8):
                dx, dy = x + d[k], y + d[k+1]
                if board[dx][dy] == 'O': queue = []; break
                if board[dx][dy] == '':
                    temp_queue.append((dx, dy))
                    board[dx][dy] = 'X'
            else:
                if not queue:
                    queue, temp_queue = temp_queue, deque([])
                    moving_count += 1

    print(moving_count)
