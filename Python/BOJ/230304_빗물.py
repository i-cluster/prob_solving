# BOJ 14719 빗물
# https://www.acmicpc.net/problem/14719

import sys
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

H, W = map(int, input().split())
heights = list(map(int, input().split()))

pool = 0
for i in range(1, W-1):
    left = max(heights[:i])
    right = max(heights[i:])
    pool += max(0, min(left, right) - heights[i])

print(pool)
