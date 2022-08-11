from pprint import pprint
import sys

sys.stdin = open("N번째 큰 수_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    list_ = list(map(int, input().split()))
    # print(list_)
    list__ = sorted(list_)
        
    print(list__[7])