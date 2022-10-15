import sys

sys.stdin = open("BOJ_1157.txt", "r")

word = input().upper()
unique = sorted(list(set(word)))
cnt = []
# print(word, unique)  # MISSISSIPI ['I', 'M', 'P', 'S']
for i in unique:
    count_word = word.count(i)
    cnt.append(count_word)
# print(cnt) # [4, 1, 1, 4]
# print(cnt.count(count_word)) # 2
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max = cnt.index(max(cnt))
    print(unique[max])
