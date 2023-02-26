# BOJ 1759 암호 만들기
# https://www.acmicpc.net/problem/1759

def crack(l, i, v, pw):
    if l == L:
        if 0 < v <= l - 2: print(pw); return

    for k in range(i, C):
        crack(l+1, k+1, v+1 if alphabet[k] in vw else v, pw + alphabet[k])


import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = sorted(list(input().split()))
vw = ['a', 'e', 'i', 'o', 'u']

crack(0, 0, 0, '')
