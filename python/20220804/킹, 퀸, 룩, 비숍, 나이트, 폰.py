import sys

sys.stdin = open("킹, 퀸, 룩, 비숍, 나이트, 폰_input.txt")

chess_pieces = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))

for i in range(len(n)):
    # print(i)
    # print(chess_pieces[i], end = ' ') # 1 1 2 2 2 8
    # print(n[i], end = ' ') # 0 1 2 2 2 7
    print(chess_pieces[i] - n[i], end = ' ')