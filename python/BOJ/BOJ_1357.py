import sys

sys.stdin = open("BOJ_1357.txt", "r")


a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(int(str(a + b)[::-1]))
