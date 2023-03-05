# BOJ 1890 점프
# https://www.acmicpc.net/problem/1890

import sys, collections
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

stack = collections.deque([(0, 0)])
d = [0, 1, 0]

arrive = 0
while stack:
    i, j = stack.popleft()

    if i == j == N-1: arrive += 1
    else:
        jump = board[i][j]
        for k in range(2):
            di, dj = i + d[k]*jump, j + d[k+1]*jump
            if di < N and dj < N: stack.append((di, dj))

print(arrive)
