import sys
sys.stdin = open('BOJ_10818.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))