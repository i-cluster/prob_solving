# BOJ 11729 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

# 시작 위치 i, 도착 위치 j, 남은 위치 m, 원판 수 n
def moving(i, j, m, n):
    if n == 1:
        print(i, j); return

    # n-1개 원판 옆으로 옮기기
    moving(i, m, j, n-1)
    print(i, j)
    moving(m, j, i, n-1)


import sys

N = int(sys.stdin.readline())
print(2 ** N - 1)
moving(1, 3, 2, N)
