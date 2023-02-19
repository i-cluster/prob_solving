# BOJ 10844 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

import sys
input = sys.stdin.readline

# 끝 자릿수 0~9 [0 / 0 1 2 3 4 5 6 7 8 9 / 0]
last_num = [0, 0] + [1] * 9 + [0]
for _ in range(int(input())-1):
    copyed = [0]
    for i in range(1, 11):
        copyed.append(last_num[i+1] + last_num[i-1])
    last_num = copyed + [0]

print(sum(last_num) % 1000000000)
