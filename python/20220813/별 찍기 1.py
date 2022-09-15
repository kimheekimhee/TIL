import sys

sys.stdin = open("별 찍기 1.txt")

N = int(input())
for tc in range(1, N + 1):
    print((tc)*'*')