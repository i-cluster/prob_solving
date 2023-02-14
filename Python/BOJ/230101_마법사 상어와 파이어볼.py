# BOJ 20056 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().split())
ball_dict = defaultdict(set)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    ball_dict[(r-1, c-1)].add((m, s, d))

di = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(K):
    # 이동 후 위치 정보
    new_dict = defaultdict(set)

    # 이동
    for rc, balls in ball_dict.items():
        r, c = rc
        for ball in balls:
            m, s, d = ball                              # 질량, 속력, 방향
            # 격자 바깥으로 나가면 반대쪽에서 등장
            dr, dc = (r + di[d][0] * s) % N, (c + di[d][1] * s) % N
            new_dict[(dr, dc)].add((m, s, d))          # 이동 후 위치정보에 넣기

    # 이동 후 위치 정보로 바꾸기
    ball_dict = new_dict

    # 볼 연산
    for rc, balls in ball_dict.items():
        l = len(balls)
        if l >= 2:
            r, c = rc
            new_balls = list(zip(*balls))               # new_balls - [[질량 정보], [속력 정보], [방향 정보]]
            new_m = sum(new_balls[0]) // 5              # 변동 후 질량 new_m
            if new_m > 0:
                new_s = sum(new_balls[1]) // l          # 변동 후 속력 new_s
                new_d = 0 if sum(new_balls[2][i] % 2 for i in range(l)) in (0, l) else 1            # 변동 후 방향
                ball_dict[(r, c)] = {(new_m, new_s, k * 2 + new_d) for k in range(0, 4)}
            else: ball_dict[(r, c)] = set()             # 질량 1 이하면 소멸

print(sum(ball[0] for balls in ball_dict.values() for ball in balls if balls))
