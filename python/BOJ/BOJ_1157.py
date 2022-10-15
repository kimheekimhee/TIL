import sys

sys.stdin = open("BOJ_1157.txt", "r")

word = input().upper()
unique = list(set(word))
cnt = []

for i in unique:
    count_word = word.count(i)
    cnt.append(count_word)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max = cnt.index(max(cnt))
    print(unique[max])
