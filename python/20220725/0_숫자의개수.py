# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(0, 10):
    print(result.count(str(i)))