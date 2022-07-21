import sys
sys.stdin = open('SWEA_2071_input.txt', 'r')

T = int(input())

for test_case in range (0, T) :
    numbers = list(map(int, input().split()))
    print(f'#{test_case + 1}', round(sum(numbers)/10))