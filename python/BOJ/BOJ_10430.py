import sys

sys.stdin = open("BOJ_10430.txt", "r")

A, B, C = map(int, input().split())

# print(a, b, c)

print((A+B)%C)

print(((A%C) + (B%C))%C)

print((A*B)%C)

print(((A%C) * (B%C))%C)