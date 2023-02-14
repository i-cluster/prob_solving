# BOJ 2292 벌집
# https://www.acmicpc.net/problem/2292

from sys import stdin
s_input = stdin.readline

N = int(s_input())

i, n = 1, 1
r = 1
while n < N:
    n += 6 * i
    r += 1
    i += 1

print(r)
