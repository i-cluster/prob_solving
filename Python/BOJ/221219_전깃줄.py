# BOJ 2565 전깃줄
# https://www.acmicpc.net/problem/2565

import sys, bisect
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

n = int(input())
# A 기준 정렬 wiresA, B 기준 정렬 wiresB
wiresA = sorted(list(tuple(map(int, input().split())) for _ in range(n)))
wiresB = sorted(wiresA, key= lambda x: x[1])

# A 기준 B 증가 구간, B 기준 A 증가 구간
dpA, dpB = [wiresA[0][1]], [wiresB[0][0]]

for i in range(1, n):
    # A 검사
    if wiresA[i][1] > dpA[-1]: dpA.append(wiresA[i][1])
    else:
        idx = bisect.bisect_left(dpA, wiresA[i][1])
        dpA[idx] = wiresA[i][1]

    # B 검사
    if wiresB[i][0] > dpB[-1]: dpB.append(wiresB[i][0])
    else:
        idx = bisect.bisect_left(dpB, wiresB[i][0])
        dpB[idx] = wiresB[i][0]

print(n - max(len(dpA), len(dpB)))
