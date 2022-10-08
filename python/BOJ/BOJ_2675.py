import sys

sys.stdin = open("BOJ_2675.txt", "r")

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end="")  # end='' 옆으로 붙임
    print()  # 줄넘김
