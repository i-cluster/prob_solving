# 2020 KAKAO BLIND RECRUITMENT, 60057 문자열 압축
# https://bit.ly/3jMfbwS

def solution(s):
    l = len(s)
    answer = len(s)

    # 단위 k
    for k in range(1, l // 2 + 1):
        i = 0
        res = ''

        # 단위 문자 unit, 카운트 cnt
        unit, cnt = s[:k], 0

        # 자르기
        while i < l:
            # 현재 단위 문자와 같으면 카운트 1 증가
            if s[i:i + k] == unit:
                cnt += 1
                i += k
            # 다르면 문자열을 결과에 넣고 단위 교체, 카운트 초기화
            else:
                res += str(cnt) + unit if cnt > 1 else unit
                unit, cnt = s[i:i + k], 0
        else:
            # 남은 문자열 넣기
            res += str(cnt) + unit if cnt > 1 else unit

        if len(res) < answer: answer = len(res)

    return answer