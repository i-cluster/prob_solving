# BOJ 11723 집합
# https://www.acmicpc.net/problem/11723

from sys import stdin

s_input = stdin.readline

i = 0
for _ in range(int(s_input())):
    s = s_input().rstrip()
    if s == 'all':
        i = (1 << 20) - 1
    elif s == 'empty':
        i = 0
    else:
        odr, n = s.split()
        n = int(n) - 1
        if odr == 'add': i |= (1 << n)
        elif odr == 'remove': i &= ~(1 << n)
        elif odr == 'toggle': i ^= (1 << n)
        else: print(1 if i & (1 << n) else 0)