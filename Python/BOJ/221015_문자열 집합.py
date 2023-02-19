# BOJ 14425 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys

s_input = sys.stdin.readline

N, M = map(int, s_input().split())
S = {s_input().strip(): 1 for _ in range(N)}

ans = 0
for _ in range(M):
    ans += S.get(s_input().strip(), 0)

print(ans)
