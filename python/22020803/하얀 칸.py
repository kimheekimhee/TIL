import sys

sys.stdin = open("하얀 칸_input.txt")

from pprint import pprint
board = []

for i in range(8):
    board.append(list(input())) # 인풋은 스트링이니까 스트링 안해도됨
pprint(board) # board 생성
count_ = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: # i + j % 2 가 0일때 하얀칸
            if board[i][j] == 'F': # 'F' 일때가 말이 올려져있는칸
                count_ += 1
print(count_)