# BOJ 2579 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

n = int(input())
stairs = list(int(input()) for _ in range(n))

score = [0, 0, stairs[0]]

for i in range(1, n):
    score.append(max(score[-3] + stairs[i-1], score[-2]) + stairs[i])

print(score[-1])
