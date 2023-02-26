# BOJ 7576 토마토
# https://www.acmicpc.net/problem/7576

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [['2'] * (M+2)]
unripe, ripe_li = 0, []
for n in range(N):
    arr = list(input().split())
    unripe += arr.count('0')
    for m in range(M):
        if arr[m] == '1': ripe_li.append((n+1, m+1))
    box.append(['2'] + arr + ['2'])
box.append(['2'] * (M+2))

day = 0
d = [0, -1, 0, 1, 0]
while unripe and ripe_li:
    new_ripe_li = []

    for rp in ripe_li:
        i, j = rp
        for k in range(4):
            di, dj = i + d[k], j + d[k+1]
            if box[di][dj] == '0':
                box[di][dj] = '1'
                unripe -= 1
                new_ripe_li.append((di, dj))

    ripe_li = new_ripe_li
    day += 1

if not unripe: print(day)
else: print(-1)
