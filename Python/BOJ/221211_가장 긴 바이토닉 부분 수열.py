# BOJ 11054 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054

import sys, bisect
from collections import deque
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dpInc, dpDec = [seq[0]], [seq[-1]]
dpInc_len, dpDec_len = deque(), deque()

for i in range(N):
    # 증가 수열 체크
    if seq[i] > dpInc[-1]:
        idx = len(dpInc)
        dpInc.append(seq[i])
    else:
        idx = bisect.bisect_left(dpInc, seq[i])
        dpInc[idx] = seq[i]

    dpInc_len.append(idx+1)

    # 감소 수열 체크
    if seq[-i-1] > dpDec[-1]:
        idx = len(dpDec)
        dpDec.append(seq[-i-1])
    else:
        idx = bisect.bisect_left(dpDec, seq[-i-1])
        dpDec[idx] = seq[-i-1]

    dpDec_len.appendleft(idx+1)

print(max(list(x + y for x, y in zip(dpInc_len, dpDec_len)))-1)
