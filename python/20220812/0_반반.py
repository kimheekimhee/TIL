import sys

sys.stdin = open("_반반.txt")

tc = int(input())

for test_case in range(1, tc + 1):
    s = input()
    # print(s)
    s_ = sorted(s)
    # print(s_)
    # print(s_[0], s_[1])
    if s_[0] == s_[1] and s_[2] == s_[3] and s_[0] != s_[2]:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')