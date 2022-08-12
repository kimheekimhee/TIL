import sys
from xml.dom import WrongDocumentErr

sys.stdin = open("_모음이보이지않는사람.txt")

tc = int(input())

for test_case in range(1, tc + 1):
    word = input()
    # print(word)
    word_ = word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    print(f'#{test_case} {word_}')