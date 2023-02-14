# BOJ 12865 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
goods = [(0,)] + list(tuple(map(int, input().split())) for _ in range(N))

# dp = list([0] * (K+1) for _ in range(N+1))

# for i in range(1, K+1):
#     # 물건 하나씩 넣어보기
#     for j in range(1, N+1):
#         # j번째 물건 넣기
#         if goods[j][0] > i:
#             # 물건 넣을 수 없음
#             dp[j][i] = dp[j-1][i]
#         else:
#             # 물건 넣을 수 있음
#             # j번째 물건 무게 만큼 가방을 비웠을 때 담을 수 있는 최대 무게 -> dp[j-1][i-(j번째 무게)]
#             dp[j][i] = max(dp[j-1][i-goods[j][0]] + goods[j][1], dp[j-1][i])
#
# print(dp[-1][-1])


dp = [0] * (K+1)

# i번째 물건 넣기
for i in range(1, N+1):
    # 가방 용량이 i 무게보다 작을 때는 변동 없음
    for j in range(K, goods[i][0]-1, -1):
        dp[j] = max(dp[j-goods[i][0]] + goods[i][1], dp[j])

print(dp[-1])
