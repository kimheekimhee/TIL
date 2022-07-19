# import sys
# sys.stdin = open('SWEA_2071_input.txt', 'r')

T = int(input())

for test_case in range (1, T + 1) :
    numbers = list(map(int, input().split()))
    print('#' + str(test_case), round(sum(numbers)/10))