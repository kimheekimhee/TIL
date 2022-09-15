import sys
sys.stdin = open('BOJ_2742.txt', 'r')

n = int(input())
n_ = []
for i in range(1, n + 1):
    n_.append(i)

n__ = reversed(n_)

for i in n__:
    print(i)