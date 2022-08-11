import sys

sys.stdin = open("피시방 알바_input.txt")

N = int(input()) # 손님 수

A = list(map(int, input().split())) # 앉으려는 자리

x = len(list(set(A))) # 앉으려는 자리 중복 제거 후 갯수

print(N-x) # 손님 수 빼기 앉으려는 자리 중복 제거 후 갯수
print(x)