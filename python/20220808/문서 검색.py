import sys

sys.stdin = open("문서 검색_input.txt")

a = input()
b = input()
cnt = 0
n = 0
while n <= len(a) - len(b):
    if a[n:n + len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1
print(cnt)