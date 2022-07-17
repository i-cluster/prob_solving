# 2020 KAKAO BLIND RECRUITMENT, 60061 기둥과 보 설치
# https://bit.ly/2W0XrET

# 유효성 검사
# 좌표 x y, 공간 sp, 기둥/보 k
def check(x, y, sp, k):
    # 기둥
    if k == 0:
        # 바닥 or 보 한쪽 끝 or 다른 기둥 위
        if y == 1 or '1' in sp[y][x - 1] or '1' in sp[y][x] or '0' in sp[y - 1][x]: return '0'

    # 보
    else:
        # 기둥 위 or 양쪽 보
        if '0' in sp[y - 1][x] or '0' in sp[y - 1][x + 1] or ('1' in sp[y][x - 1] and '1' in sp[y][x + 1]): return '1'

    return False


# 삭제 검사
# 좌표 x y, 공간 sp, 기둥/보 k, 설치 좌표 리스트 ans
def del_check(x, y, sp, k, ans):
    # 일단 없애
    sp[y][x] = sp[y][x].replace(k, '')

    # 검사 리스트 : 기동 - 위쪽 기둥, 왼쪽 보, 오른쪽 보 / 보 - 왼쪽 기둥, 오른쪽 기둥, 왼쪽 보, 오른쪽 보
    ck_list = [('0', x, y + 1), ('1', x - 1, y + 1), ('1', x, y + 1)] if not int(k) else [('0', x, y), ('0', x + 1, y),
                                                                                          ('1', x - 1, y),
                                                                                          ('1', x + 1, y)]

    for r, i, j in ck_list:
        if r in sp[j][i] and not check(i, j, sp, int(r)):
            sp[y][x] += k
            break
    else:
        ans.remove([x - 1, y - 1, int(k)])

    return sp, ans


def solution(n, build_frame):
    # 공간
    space = list([''] * (n + 3) for _ in range(n + 3))
    answer = []

    for frame in build_frame:
        # 가로 x, 세로 y, 기둥/보 a, 삭제/설치 b
        x, y, a, b = frame
        x += 1;
        y += 1

        # 설치 : 기둥 'P', 보 'B'
        if b == 1:
            try:
                space[y][x] += check(x, y, space, a)
                answer.append([x - 1, y - 1, a])
            except:
                pass

        # 삭제
        else:
            space, answer = del_check(x, y, space, str(a), answer)

    return sorted(answer)