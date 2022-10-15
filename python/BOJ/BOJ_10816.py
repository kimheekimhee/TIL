import sys
from collections import Counter

sys.stdin = open("BOJ_10816.txt", "r")

N = int(input())
card_numbers = map(int, input().split())
M = int(input())
numbers = map(int, input().split())

