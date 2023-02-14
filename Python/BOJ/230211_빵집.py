# BOJ 3109 빵집
# https://www.acmicpc.net/problem/3109

def install(r, c):
    if c == C: return 1

    for i in range(3):
        dr, dc = r + d[i], c + 1
        if field[dr][dc] == '.':
            field[dr][dc] = 'o'
            if install(dr, dc): return 1


import sys
input = sys.stdin.readline

R, C = map(int, input().split())
field = [['x'] * (C+2)] + [['x'] + list(input()) + ['x'] for _ in range(R)] + [['x'] * (C+2)]

d = [-1, 0, 1]
pipe_cnt = 0
for k in range(1, R+1):
    pipeline = install(k, 1)
    if pipeline: pipe_cnt += 1

print(pipe_cnt)
