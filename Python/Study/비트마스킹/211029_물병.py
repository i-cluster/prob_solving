# BOJ 1052
# https://www.acmicpc.net/problem/1052

# from sys import stdin
# s_input = stdin.readline

import sys
sys.stdin = open('../../sample.txt', 'r')

for i in range(int(input())):
    # 현재 물병 N, 목표 물병 K
    N, K = map(int, input().split())
    binN = format(N, 'b')
    l = len(binN)

    # 물병 c
    cnt = 1
    for i in range(1, l):
        if cnt == K:
            print((1 << (l - i)) - int('0b' + binN[i:], 2))
            break
        if binN[i] == '1': cnt += 1
    else: print(0)

    # if K >= binN.count('1'): print(0)
    # else:
    #     i = int('0b' + binN[K:], 2)
    #     print((1 << (len(binN) - K)) - i if i else i)


'''
5개, 2개 -> 101
'''
