import sys

sys.stdin = open("BOJ_10798.txt", "r")

words = []
for _ in range(5):
    word=input()
    words.append(word)
print(words)
for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')