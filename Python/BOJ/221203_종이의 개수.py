# BOJ 1931 회의실 배정
# https://www.acmicpc.net/problem/1780

# 시작 행 i, 시작 열 j, 크기 n
def check(i, j, n):
    global res

    p = paper[i][j]
    for x in range(n):
        for y in range(n):
            if paper[i+x][j+y] != p:
                for ix in range(i, i+n, n//3):
                    for iy in range(j, j+n, n//3):
                        check(ix, iy, n//3)
                return

    res[paper[i][j]] += 1

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(input().split()) for _ in range(N)]

res = {"-1": 0, "0": 0, "1": 0}
check(0, 0, N)

for v in res.values(): print(v)
