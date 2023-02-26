# BOJ 2225 합분해
# https://www.acmicpc.net/problem/2225

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [1] * (N+1)

for _ in range(2, K+1):
    for i in range(1, N+1):
        dp[i] = dp[i-1] + dp[i]

print(dp[-1] % 1000000000)
