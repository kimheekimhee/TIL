import sys
sys.stdin = open('BOJ_10953_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split(','))
    print(a + b)