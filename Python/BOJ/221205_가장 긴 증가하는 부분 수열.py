# BOJ 11053 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys, bisect
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

# 길이별 가장 작은 증가 수열의 마지막 값
dp = [seq[0]]

for i in range(N):
    # 현재 값이 가장 크다면 마지막에 배치 (수열 길이 +1)
    if seq[i] > dp[-1]:
        dp.append(seq[i])
    # 현재 값이 마지막 값으로 끝날 수 있는 증가 수열을 찾아서 교체
    else:
        idx = bisect.bisect_left(dp, seq[i])
        dp[idx] = seq[i]

print(len(dp))
