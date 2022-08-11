import sys

sys.stdin = open("SASA 모형을 만들어보자_input.txt")

S, A = map(int, input().split())
N = S
M = A
# print(N, M)
N_ = N // 2
M_ = M // 2
# print(N_, M_)
if N > M:
    print(M_)
if N < M:
    print(N_)
if N == M:
    print(N_)