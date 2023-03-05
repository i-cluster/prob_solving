# BOJ 17135 캐슬 디펜스
# https://www.acmicpc.net/problem/17135

import sys
from collections import defaultdict
from itertools import combinations
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

N, M, D = map(int, input().split())
field, enemy = [], []
for n in range(N):
    row = list(input().split())
    enemy.extend([(n, m) for m in range(M) if row[m] == '1'])
    field.append(row)

# distances = [sorted(list((N - e[0] + abs(i - e[1]), e[0], e[1]) for e in enemy)) for i in range(M)]
rounds = [sorted(list((max(N-e[0] + abs(i-e[1]) - D, 0), e[0], e[1]) for e in enemy)) for i in range(M)]

kill_count = list(k for k in range(N))

position = list(combinations([x for x in range(M)], 3))
for a, b, c in position:
    pass
