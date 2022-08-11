import sys

sys.stdin = open("공_input.txt")

N = int(input())

cups = [1,2,3]
for _ in range(N):
    # 변경되는 두 컵의 위치 입력
    x, y = map(int, input().split())
    # print(x, y)
    # 3 1
    # print(cups.index(x), cups.index(y))
    # 2 0
    # xi yi 를 입력된 cups의 인덱스로 변경
    xi = cups.index(x)
    yi = cups.index(y)
    # print(xi, yi)
    # 2 0
    # xi를 yi로, yi를 xi로 변경
    # cups.index(x) = cups.index(y)
    # cups.index(y) = cups.index(x)
    cups[xi], cups[yi] = cups[yi], cups[xi]
    
print(cups[0])