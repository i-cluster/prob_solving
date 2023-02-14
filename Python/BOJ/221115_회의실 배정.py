# BOJ 1931 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

meetings = sorted(list(list(map(int, input().split())) for _ in range(int(input()))), key= lambda x: (x[1], x[0]))

e = meetings[0][1]
i, cnt = 1, 1
while i < len(meetings):
    if meetings[i][0] >= e:
        e = meetings[i][1]
        cnt += 1

    i += 1

print(cnt)
