import sys

sys.stdin = open("_퍼펙트셔플.txt")

tc = int(input())
word_ = []
for test_case in range(1, tc + 1):
    n = int(input())
    word = list(input().split())
    # print(n)
    # print(word)
    # print(len(word))
    word_1 = word[0:n//2]
    word_2 = word[n//2:len(word)]
    print(word_1, word_2)
    print(f'#{test_case}')
