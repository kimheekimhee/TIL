import sys
sys.stdin = open('BOJ_11720.txt', 'r')

a = int(input())
n = list(input())
sum = 0
for i in n:
    sum += int(i)
print(sum)