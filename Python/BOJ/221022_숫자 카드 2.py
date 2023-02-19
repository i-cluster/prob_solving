# BOJ 10816 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys
from collections import defaultdict
s_input = sys.stdin.readline

N, li_N = int(s_input()), list(s_input().split())
dic_N = defaultdict(int)
for i in range(N):
    dic_N[li_N[i]] += 1

M, li_M = int(s_input()), list(s_input().split())
for j in range(M):
    print(dic_N.get(li_M[j], 0), end=' ')
