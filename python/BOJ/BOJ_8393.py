import sys
sys.stdin = open('BOJ_8393.txt', 'r')

n = int(input())

sum_ = 0
for i in range(1, n + 1):
    sum_ += i
print(sum_)