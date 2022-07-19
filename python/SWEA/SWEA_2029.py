# 문제 풀 때 vs code 를 해당 폴더에서 열기
# 로컬에서 코드를 작성할때 텍스트 파일을 받아서 아래 두 줄 입력
# 제출하기 전에는 주석처리

# import sys
# sys.stdin = open('SWEA_2029_input.txt', 'r')

T = int(input()) # 3

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range (1, T + 1) :
    T += 1
    a1, a2 = map(int, input().split())
    print('#' + str(test_case), a1 // a2, a1 % a2)