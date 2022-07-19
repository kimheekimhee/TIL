# import sys
# sys.stdin = open('SWEA_2070_input.txt', 'r')

T = int(input())

for test_case in range (1, T + 1) :
    a1, a2 = map(int, input().split())

    if a1 < a2:
        print('#' + str(test_case), '<')
    if a1 == a2:
        print('#' + str(test_case), '=')
    if a1 > a2:
        print('#' + str(test_case), '>')