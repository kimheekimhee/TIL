from pprint import pprint
import sys

sys.stdin = open("단어 뒤집기_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    list_ = list(input().split())
    # print(list_[::-1])
    for i in list_:
        print(i[::-1], end = ' ')
    print()