# BOJ 1654 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = sorted(list(int(input()) for _ in range(K)))

i, j = lans[0] // N, sum(lans) // N + 1

while j > i:
    # 중간 값 m, 랜선 수 n
    m = (i+j) // 2
    n = sum(lan // m for lan in lans)
    # i, j가 1 차이라면 종료
    if m == i: break
    # N보다 같거나 크면 i ->, 작으면 <- j
    elif n >= N: i = m
    elif n < N: j = m

print(i)
