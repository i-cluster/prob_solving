# BOJ 11066 파일 합치기
# https://www.acmicpc.net/problem/11066

import sys
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))

    novel = [0, files[0]]
    for i in range(1, K):
        # novel.append(min(novel[-1] * 2 + files[i], (novel[-2] + files[i-1] + files[i]) * 2))
        # novel.append(sum(novel[j], files[j+1:i]) for j in range(i))

        min_val = novel[-1] + files[i]
        novel_rev = [0, files[i]]
        for j in range(1, i):
            res = min(novel[j], novel_rev[j])
            novel_rev.append()
            if res < min_val: min_val = res

    print(novel)
