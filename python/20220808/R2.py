import sys

sys.stdin = open("R2_input.txt")

a, avg = map(int, input().split())
print(a, avg)
b = avg * 2 - a
print(b)