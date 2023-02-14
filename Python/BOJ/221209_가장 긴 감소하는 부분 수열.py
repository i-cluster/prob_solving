# BOJ 11722 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722

import sys, bisect
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [seq[-1]]

for i in range(N-1, -1, -1):
    if seq[i] > dp[-1]:
        dp.append(seq[i])
    else:
        idx = bisect.bisect_left(dp, seq[i])
        dp[idx] = seq[i]

print(len(dp))
