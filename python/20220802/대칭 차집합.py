import sys

sys.stdin = open("대칭 차집합_input.txt")

n, m = map(int, input().split()) # n, m 각각의 원소의 개수
a = set(map(int, input().split())) # a 로 set
# print(a) # {1, 2, 4}
b = set(map(int, input().split())) # b 로 set
# print(b) # {2, 3, 4, 5, 6}
# print(len(a) # 3, len(b) # 5)
# print(len(a-b) # 1, len(b-a) # 3)
print(len(a-b)+len(b-a))