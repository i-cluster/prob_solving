# BOJ 1722 순열의 순서
# https://www.acmicpc.net/problem/1722

import math
# from sys import stdin
# s_input = stdin.readline

import sys
sys.stdin = open('../../testcase.txt', 'r')


def find_k(x, N, order):
    for i in range(1, x):
        if check_num[i] == 0:
            order += math.factorial(N)

    return order, N-1


def find_arr(a, t, n, m, ans):
    i, j = t // math.factorial(n), t % math.factorial(n)
    if i == 0:
        m += 1
    else:
        for l in range(m, N+1):
            if check_num[l] == 0:
                if i == 0:
                    check_num[l] = 1
                    return
                i -= 1


for i in range(int(input())):
    N = int(input())
    k, *arr = map(int, input().split())
    check_num, n = list(0 for i in range(N+1)), N - 1

    if k == 1:
        ans, a = [], arr[0] - 1
        m = 1
        while a:
            i, j = a // math.factorial(n), a % math.factorial(n)
            t = m
            if i == 0:
                m += 1
            else:
                for l in range(m, N+1):
                    if check_num[l] == 0:
                        if i == 0: t = l; break
                        i -= 1

            check_num[t], a = 1, j
            n -= 1
            ans += [t]

        ans += list(i for i in range(1, N+1) if check_num[i] == 0)

        # t = arr[0]
        # while t:
        #     t = 0
        # ans = []
    else:
        ans = 1
        for x in arr:
            ans, n = find_k(x, n, ans)
            check_num[x] = 1

    print(ans)
