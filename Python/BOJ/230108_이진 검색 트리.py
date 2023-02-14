# BOJ 5639 이진 검색 트리
# https://www.acmicpc.net/problem/5639

import sys
# input = sys.stdin.readlines
# sys.stdin = open('../testcase.txt', 'r')


def postorder(n):
    if tree[n][0]: postorder(tree[n][0])
    if tree[n][1]: postorder(tree[n][1])
    print(n)


preorder = [int(line) for line in sys.stdin.readlines()]
tree = {i: [0, 0] for i in preorder}

for n in preorder:
    r = preorder[0]
    while 1:
        if n == r: break
        if n < r:
            if not tree[r][0]: tree[r][0] = n; break
            else: r = tree[r][0]
        else:
            if not tree[r][1]: tree[r][1] = n; break
            else: r = tree[r][1]

print(tree)
postorder(preorder[0])
