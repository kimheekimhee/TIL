import sys

sys.stdin = open("크로아티아_알파벳_input.txt")

word = input()
# print(len(word))
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for char in alphabet:
    # if char in word:
    word = word.replace(char, 'a')
print(len(word))