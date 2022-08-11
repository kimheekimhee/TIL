import sys

sys.stdin = open("뜨거운 붕어빵_input.txt")

N, M = map(int, input().split())
# print(N, M)
fish = []
for _ in range(N):
    fish.append(input())
# print(fish)
for __ in fish:
    print(__[::-1])