import sys

sys.stdin = open("단어_공부_input.txt")
word = input()
list_ = []
for i in word:
    list_.append(i)
print(list_, type(list_))
print(str(list_), type(str(list_)))
for i in list_:
    i = str(i)
print(list_,type(list_))
