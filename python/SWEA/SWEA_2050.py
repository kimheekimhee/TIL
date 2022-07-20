import sys
sys.stdin = open('SWEA_2050_input.txt', 'r')

word = list(input())

for c in word:
    print(ord(c)-64, end = ' ')