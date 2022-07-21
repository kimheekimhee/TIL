import sys
sys.stdin = open('SWEA_1986_input.txt', 'r')

T = int(input())
for tt in range(T):
    n = int(input())
    s = 0
    for j in range(1,n+1):
        if j % 2 == 0:
            s -= j
        else:
            s += j
    print(f"#{tt+1}", s)