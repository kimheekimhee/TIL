from pprint import pprint
import sys

sys.stdin = open("대표값_input.txt")

numbers = list(int(input()) for i in range(10))
# print(numbers)
sum_numbers_ = sum(numbers)
print(sum_numbers_//10)
# print(max(numbers)) << 최댓값
print(max(numbers, key = numbers.count))