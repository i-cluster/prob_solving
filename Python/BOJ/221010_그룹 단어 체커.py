# BOJ 1316 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

from sys import stdin
s_input = stdin.readline

cnt = 0
for _ in range(int(s_input())):
    checker = [0] * 26
    word = str(s_input().strip())
    
    i = word[0]
    for w in word:
        if checker[ord(w) - 97] and i != w: break
        else: checker[ord(w) - 97] = 1; i = w
    else: cnt += 1

print(cnt)
