# 2021 카카오 채용연계형 인턴십, 81302 거리두기 확인하기
# https://bit.ly/3tusHsh

d = [0, -1, 0, 1, 0]


def distancing(n, i, j, si, sj, place):
    if n:
        for k in range(4):
            di, dj = i + d[k], j + d[k + 1]
            if 0 <= di <= 4 and 0 <= dj <= 4 and (di, dj) != (si, sj):
                # 빈 테이블
                if place[di][dj] == 'O':
                    if not distancing(n - 1, di, dj, i, j, place): return False
                # 응시자
                elif place[di][dj] == 'P':
                    print(si, sj)
                    return False

    return True


def searching(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not distancing(2, i, j, i, j, place): return 0

    return 1


def solution(places):
    return list(searching(places[i]) for i in range(5))