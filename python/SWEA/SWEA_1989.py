# import sys
# sys.stdin = open('SWEA_1989_input.txt', 'r')

T = int(input())
for i in range(1, T + 1):
    word = list(input())
    
    
    if word == list(reversed(word)):
        print(f'#{i}', 1)
    else:
        print(f'#{i}', 0)