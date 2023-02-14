# BOJ 2580 스도쿠
# https://www.acmicpc.net/problem/2580

def solving(s):
    if s == -1:
        [print(*row) for row in sudoku]
        print(f'execution: {time.time() - start} sec')
        exit(0)

    # 행 좌표 i, 열 좌표 j
    i, j = cells[s]
    chk_set = set(k for k in range(1, 10))

    # 들어갈 수 있는 숫자 확인하기
    # 행 체크
    chk_set -= set(sudoku[i])
    # 열 체크
    chk_set -= set(sudoku[k][j] for k in range(9))

    # 사각형 체크
    pi, pj = (i // 3) * 3, (j // 3) * 3
    chk_set -= set(sudoku[di][dj] for di in range(pi, pi+3) for dj in range(pj, pj+3))

    # 가능한 숫자가 있다면 다음 셀로 이동
    for val in chk_set:
        sudoku[i][j] = val
        solving(s-1)
        sudoku[i][j] = 0


import sys, time
# input = sys.stdin.readline
sys.stdin = open('../testcase.txt', 'r')

start = time.time()

sudoku, cells = [], []
for i in range(9):
    arr = list(map(int, input().split()))
    for j, el in enumerate(arr):
        if el == 0: cells.append((i, j))
    sudoku.append(arr)

d = [0, 0, 1, 0, -1, 1, 1, -1, -1, 0]

solving(len(cells)-1)
