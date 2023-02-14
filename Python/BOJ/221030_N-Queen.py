# BOJ 9663 N-Queen
# https://www.acmicpc.net/problem/9663

N = int(input())
y_line, cross_xline, cross_yline = [0] * N, dict(), dict()
cnt = 0


def check(x):
    if x == N: global cnt; cnt += 1; return

    # 열 선택
    for y in range(N):
        if y_line[y] == cross_xline.get(x-y, 0) == cross_yline.get(x+y, 0) == 0:
            y_line[y] = cross_xline[x-y] = cross_yline[x+y] = 1
            check(x+1)
            y_line[y] = cross_xline[x-y] = cross_yline[x+y] = 0


check(0)
print(cnt)
