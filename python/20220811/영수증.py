import sys

sys.stdin = open("영수증.txt")

X = int(input())
N = int(input())
count_ = 0
for _ in range(N):
    a, b = map(int,input().split())
    # print(a, b)
    count_ += a * b
if count_ == X:
    print('Yes')
else:
    print('No')