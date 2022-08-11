# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("4_나는요리사다.txt")


for test_case in range(0, 4):
    score = int(input().split())
    score_sum = 0
    for i in score:
        i += score_sum
    print(score_sum)
