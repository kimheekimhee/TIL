# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for t in range(T):
    
    ox = input()

    count_o = 1
    sum_ = 0

    for answer in ox:
        if answer == 'O':
            sum_ = count_o + sum_
            count_o += 1
        if answer == 'X':
            count_o = 0
    print(sum_)