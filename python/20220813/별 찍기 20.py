import sys

sys.stdin = open("별 찍기 20.txt")

N = int(input())
for tc in range(1, N + 1):
    if tc % 2 == 0:
        print(' *' * N)
    else:
        print('* ' * N)