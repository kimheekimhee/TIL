import sys
sys.stdin = open('BOJ_2739.txt', 'r')

n = int(input())

for i in range (1, 9 + 1):
    print(f'{n} * {i} = {n * i}')