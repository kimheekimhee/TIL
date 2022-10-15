import sys

sys.stdin = open("BOJ_5622.txt", "r")

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
time = 0
# print(len(dial)) << 8
for i in range(len(dial)):
    # print(i) << 0 1 2 3 4 5 6 7
    for w in word:
        # print(w) << W A 8번 출력
        # print(dial[i]) << ABC ABC DEF DEF ...
        if w in dial[i]:
            time += 3 + i  # 0 == 3, 1 == 4 ...
print(time)  # W = 10, A =3
