# BOJ 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

def calculate(i, rs):
    if i == N:
        global max_res, min_res
        max_res, min_res = max(max_res, rs), min(min_res, rs)
        return

    n = nums[i]
    for k in range(4):
        if cals[k]:
            cals[k] -= 1
            if k == 0: cal_res = rs + n
            elif k == 1: cal_res = rs - n
            elif k == 2: cal_res = rs * n
            else: cal_res = -(-rs // n) if rs < 0 else rs // n
            calculate(i+1, cal_res)
            cals[k] += 1


import sys
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
cals = list(map(int, input().split()))

max_res, min_res = - (10 ** 9), 10 ** 9

calculate(1, nums[0])

print(max_res, min_res)
