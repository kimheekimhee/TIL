import sys

sys.stdin = open("BOJ_1157.txt", "r")

word = input().upper()
unique = list(set(word))
cnt = []
# print(word, unique) << MISSISSIPI ['S', 'P', 'M', 'I']
for i in unique:
    count_word = word.count(i)
    cnt.append(count_word)
print(cnt)
print(cnt.count(count_word))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max = cnt.index(max(cnt))
    print(unique[max])
