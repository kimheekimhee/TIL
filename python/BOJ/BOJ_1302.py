import sys

sys.stdin = open("BOJ_1302.txt", "r")

N = int(input())

for i in range(1, N + 1):
    book_name = input()
    print(book_name)
