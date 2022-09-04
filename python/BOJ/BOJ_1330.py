import sys
sys.stdin = open('BOJ_1330.txt', 'r')

a, b = map(int, input().split())

if a > b:
    print('>')
elif a == b:
    print('==')
elif a < b:
    print('<')