import sys

sys.stdin = open("얼마_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    s = int(input())
    n = int(input())
    price = s
    for _ in range(1, n + 1):
        q, p = map(int, input().split())
        price += q * p
    print(price)