import sys

sys.stdin = open("BOJ_1085.txt", "r")

x, y, w, h = map(int, input().split())

print(x, y, w, h)

print(min(x, y, h-y, w-x))