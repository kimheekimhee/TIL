import sys
from collections import Counter

sys.stdin = open("BOJ_10812.txt", "r")


n, m = map(int, input().split())
I = [i+1 for i in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    I[i-1:j] = I[k-1:j] + I[i-1:k-1]
print(*I)