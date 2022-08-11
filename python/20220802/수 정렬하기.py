import sys

sys.stdin = open("수 정렬하기_input.txt")

N = int(input())
n_list = []
# print(range(N))
# print(N)
# print(int(input()))
for i in range(N):
    n_list.append(int(input()))
# print(n_list)
n_list.sort()

# print(n_list, len(n_list), range(len(n_list)))
for i in range(len(n_list)):
    print(n_list[i])