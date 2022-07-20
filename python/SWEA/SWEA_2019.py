import sys
sys.stdin = open('SWEA_2019_input.txt', 'r')

number = int(input())

for i in range(0, number + 1):
    print(2 ** i, end = ' ')