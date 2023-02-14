# BOJ 14501 퇴사
# https://www.acmicpc.net/problem/14501

def consult(pay, d):
    global profit
    if d > N:
        if sum(pay) > profit: profit = sum(pay)
        return

    if d + schedule[d][0] - 1 <= N : consult(pay + [schedule[d][1]], d + schedule[d][0])
    consult(pay, d+1)


import sys

N = int(input())
schedule = [''] + list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))

profit = 0
consult([], 1)

print(profit)
