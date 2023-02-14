# BOJ 3273 두 수의 합
# https://www.acmicpc.net/problem/3273

import sys
input = sys.stdin.readline

N, arr, X = int(input()), sorted(list(map(int, input().split()))), int(input())

i, j = 0, N-1
res = 0
while i < j:
    if arr[i] + arr[j] == X:
        res += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] > X:
        j -= 1
    else:
        i += 1

print(res)
