# BOJ 2206 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys, collections
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

N, M = map(int, input().split())
field = [['2'] * (M+2)] + [['2'] + list(input()) + ['2'] for _ in range(N)] + [['2'] * (M+2)]

# 벽을 부순 세계 visit[0], 벽을 부수지 않은 세계 visit[1]
visit = [[[0] * (M+2) for _ in range(N+2)] for _ in range(2)]

d = [0, 1, 0, -1, 0]
queue = collections.deque([(1, 1, 1)])                      # (i, j, hammer)
while queue:
    i, j, hammer = queue.popleft()

    for k in range(4):
        di, dj = i + d[k], j + d[k+1]

        if hammer: continue

# visit[1][1] = (1, 1)
# flag = False
# queue = collections.deque([(1, 1, 1)])
# while queue:
#     i, j, hammer = queue.popleft()
#     if (i, j) == (N, M): flag = True
#
#     # 벽을 부순 경로 dist1, 벽을 부수지 않은 경로 dist2
#     dist1, dist2 = visit[i][j]
#
#     for k in range(4):
#         di, dj = i + d[k], j + d[k+1]
#
#         t_dist1, t_dist2 = visit[di][dj]
#         # 벽을 부순 경로 체크
#         if not hammer:
#             if field[di][dj] == '0' and dist1 < t_dist1:
#         # 벽을 부수지 않은 경로 체크
#         else:
#         # 벽이 아니라면 1) 더 짧은 경로 2) 길이가 같으면 망치 안 쓴 루트
#         if field[di][dj] == '0' and dist < t_dist or (dist == t_dist and hammer > t_hammer):
#             visit[di][dj] = (dist, hammer)
#             queue.append((di, dj))
#         # 벽이라면 1) 망치가 남아 있고 2) 부쉈을 때 더 빠른 루트 저장
#         elif field[di][dj] == '1' and hammer and dist < t_dist:
#             visit[di][dj] = (dist, 0)
#             queue.append((di, dj))
#
# [print(*row) for row in visit]
# if flag: print(visit[N][M][0])
# else: print(-1)
