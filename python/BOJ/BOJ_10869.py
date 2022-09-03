import sys
sys.stdin = open('BOJ_10869.txt', 'r')

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
