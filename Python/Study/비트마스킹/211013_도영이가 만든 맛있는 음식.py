# BOJ 2961 집합
# https://www.acmicpc.net/problem/2961

# 요리
def cook(k, j, sel):
    if not k:
        # 신맛 s, 쓴맛 b
        sel = format(sel, 'b')[::-1]
        s, b = 1, 0
        for i in range(len(sel)):
            if sel[i] == '1':
                s *= ing_li[i][0]
                b += ing_li[i][1]

        global min_v
        if abs(s-b) < min_v:
            min_v = abs(s-b)
    else:
        if j < n:
            cook(k-1, j+1, sel | (1 << j))
            cook(k, j+1, sel)


from sys import stdin
s_input = stdin.readline

n = int(s_input())
ing_li = [tuple(map(int, s_input().split())) for _ in range(n)]

min_v = 1000000000
for i in range(1, n+1):
    cook(i, 0, 0)

print(min_v)