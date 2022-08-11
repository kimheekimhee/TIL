import sys

sys.stdin = open("연속구간.txt")

list_1 = []
list_2 = []
list_3 = []

for _ in range(3):
    word = input()
    # print(word)
    print(word[0])