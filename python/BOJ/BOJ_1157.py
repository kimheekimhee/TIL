import sys

sys.stdin = open("BOJ_1157.txt", "r")


word = input()
# print(word)
list_word = []

for char in word:
    list_word.append(char)
# print(list_word)
max_char = max(list_word)

print(max_char)

max_char_count = list_word.count(max_char)

print(max_char_count)
