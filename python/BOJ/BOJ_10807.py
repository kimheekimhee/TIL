import sys

sys.stdin = open("BOJ_10807.txt", "r")

N = int(input())
numbers = list(map(int, input().split()))
find_number = int(input())
# print(N, numbers, find_number)
number_count = 0
for i in numbers:
    if i == find_number:
        number_count += 1
print(number_count)
