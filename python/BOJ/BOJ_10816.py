import sys

sys.stdin = open("BOJ_10816.txt", "r")

N = int(input())
card_numbers = map(int, input().split())
M = int(input())
numbers = map(int, input().split())
sorted_card_numbers = sorted(card_numbers)
sorted_numbers = sorted(numbers)
# print(sorted_card_numbers)  # << [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
# print(sorted_numbers)  # << [-10, -5, 2, 3, 4, 5, 9, 10]
count = {}

for card_number in card_numbers:
    if card_number in count:
        count[card_number] += 1
    else:
        count[card_number] = 1
print(count)
