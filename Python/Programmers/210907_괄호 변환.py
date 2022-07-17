# 2020 KAKAO BLIND RECRUITMENT, 60058 괄호 변환
# https://bit.ly/3zR7N91

# 문자열 분리
def test(word):
    cnt = 0
    # 빈 문자열이면 그대로 반환
    if not word: return '', ''

    # 스택이 0이 되면 문자열 잘라서 반환
    for i in range(len(word)):
        cnt += 1 if word[i] == '(' else -1
        if not cnt: return word[:i + 1], word[i + 1:]


def solution(p):
    u, v = test(p)
    # u가 빈 문자열이면 반환
    if not u: return ''

    # '('로 시작하면 올바른 문자열
    if u[0] == '(':
        return u + solution(v)
    # ')'로 시작하면 균형잡힌 문자열
    else:
        new_str = '(' + solution(v) + ')'
        # 앞뒤 문자 자륵고 뒤집어 붙이기
        for k in u[1:-1]:
            if k == '(':
                new_str += ')'
            else:
                new_str += '('
        return new_str