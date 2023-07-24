import sys

sys.stdin = open("BOJ_2566.txt", "r")

max_num = 0

for i in range(9):
    row = list(map(int, input().split()))
    if max(row) > max_num:
        max_num = max(row)
        x = i + 1
        y = row.index(max_num) + 1
print(max_num)
print(x,y)