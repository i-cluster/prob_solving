# BOJ 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

from sys import stdin
s_input = stdin.readline

# import sys
# sys.stdin = open('../testcase.txt', 'r')

arr = s_input().strip()
word_dic = {'=': ['c', 'z', 's'], '-': ['d', 'c'], 'j': ['l', 'n']}

i = len(arr) - 1
cnt = 0

# 역순으로 확인
while i > 0:
    if arr[i] in word_dic.keys() and arr[i-1] in word_dic[arr[i]]:
        cnt += 1
        # 'dz=' 처리
        if arr[i-1:i+1] == 'z=' and i-2 >= 0 and arr[i-2] == 'd': i -= 3
        else: i -= 2
    else:
        cnt += 1
        i -= 1

if i == 0: cnt += 1

print(cnt)
