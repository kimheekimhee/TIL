import sys

sys.stdin = open("꼬리를 무는 숫자 나열.txt")

a, b = map(int, input().split())
x1 = (a-1)//4 + 1 # (11-1)/(4+1) = 2
y1 = (a-1)%4 # (11-1)/4 = 2, 2
x2 = (b-1)//4 + 1 # (33-1)/(4+1) = 6
y2 = (b-1)%4 # (33-1)/4 = 8, 0
print(abs(x2-x1) + abs(y2-y1)) # 절대값(6-2) # 4 + 절대값(0-2) # 2 = 8
print(a, b)
print(x1, y1, x2, y2)