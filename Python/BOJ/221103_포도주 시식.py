# BOJ 2156 포도주 시식
# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())
wine = list(int(input()) for _ in range(n))

# drink[n] = n번째 잔까지 포도주 최대값
drink = [0, 0, wine[0]]

for i in range(1, n):
    # max(i-2번째 잔 X, i-1번째 잔 X, i번째 잔 X)
    drink.append(max(drink[-3] + wine[i-1] + wine[i], drink[-2] + wine[i], drink[-1]))

print(drink[-1])
