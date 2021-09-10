# 2021 카카오 채용연계형 인턴십, 81301 숫자 문자열과 영단어
# https://bit.ly/3DQyhKc

def solution(s):
    # 변환용 사전
    insp3, insp4, insp5 = {'one': '1', 'two': '2', 'six': '6'}, {'four': '4', 'five': '5', 'nine': '9', 'zero': '0'}, {'three': '3', 'seven': '7', 'eight': '8'}

    answer = ''

    i = 0
    while i < len(s):
        # try : 정수 변환
        try:
            answer += str(int(s[i]))
            i += 1
        # 문자일 경우 사전 목록에서 찾기
        except:
            for k in (3, 4, 5):
                if s[i:i + k] in eval('insp' + str(k)).keys():
                    answer += eval('insp' + str(k))[s[i:i + k]]
                    i += k
                    break

    return int(answer)