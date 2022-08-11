import sys

sys.stdin = open("모음의 개수_input.txt")

while True:
    word = list(input())
    if word == ['#']:
        break
    print(word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u')+word.count('A')+word.count('E')+word.count('I')+word.count('O')+word.count('U'))
    # print(word)