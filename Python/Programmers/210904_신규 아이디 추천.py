# 2021 KAKAO BLIND RECRUITMENT, 72410 신규 아이디 추천
# https://bit.ly/3zNAsfk

def solution(new_id):
    # 문자 검사용 데이터
    insp = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.')
    # 신규 아이디
    answer = '.'

    # 1~3 단계
    new_id += '.'
    for i in range(len(new_id) - 1):
        # 1단계
        if 65 <= ord(new_id[i]) <= 90 or 97 <= ord(new_id[i]) <= 122:
            answer += new_id[i].lower()
        elif new_id[i] in insp:
            # 3단계
            if new_id[i] == answer[-1] == '.':
                pass
            # 2단계
            else:
                answer += new_id[i]

    # 4단계
    answer = answer.strip('.')

    # 5단계
    if not answer: answer = 'a'

    # 6단계
    answer = answer[:15]
    answer = answer.strip('.')

    # 7단계
    for i in range(3 - len(answer)):
        answer += answer[-1]

    return answer