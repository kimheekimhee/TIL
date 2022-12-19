import sys

sys.stdin = open("BOJ_1001.txt", "r")

a, b = map(int, input().split())

print(a - b)
