# https://www.acmicpc.net/problem/2231
import sys

sys.stdin = open("BOJ_2231_input.txt")

N = int(input())
result = 0

for i in range(1, N + 1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if(s == N):
        result = i
        break

print(result)