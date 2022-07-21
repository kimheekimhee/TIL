import sys
sys.stdin = open('SWEA_1933_input.txt', 'r')

number = int(input())

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end = ' ')