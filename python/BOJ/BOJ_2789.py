import sys
sys.stdin = open('BOJ_2789.txt', 'r')

word = input()

for char in 'CAMBRIDGE':
    word = word.replace(char,'')
print(word)