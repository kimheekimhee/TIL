from re import L
import sys
from tkinter import W

sys.stdin = open("0의 개수_input.txt")

T = int(input())

# print(T)
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    count_ = 0
    list_ = []
    for _ in range(N, M + 1):
        list_.append(_)
    # print(list_)
    for _ in list_:
        __ = str(_)
        count_ += __.count('0')
    print(count_)