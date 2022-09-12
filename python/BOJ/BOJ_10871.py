import sys
sys.stdin = open('BOJ_10871.txt', 'r')

N, X = map(int, input().split())
numbers = list(map(int, input().split()))
list_ = []
for i in numbers:
    if i < X:
        list_.append(i)
print(*list_)