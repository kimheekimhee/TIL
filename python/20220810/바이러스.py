import sys

sys.stdin = open("삼각형 외우기.txt")

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Equilateral')
elif a + b + c == 180 and a == b or a == c or b == c:
    print('Isosceles')
elif a + b + c == 180 and a != b != c:
    print('Scalene')
else:
    print('Error')