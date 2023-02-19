import sys
from sys import stdin, stdout

s_input = stdin.readline
s_print = stdout.write

arr = list(s_input().split() for _ in range(int(s_input())))
print(arr)
