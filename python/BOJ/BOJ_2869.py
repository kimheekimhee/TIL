import sys
sys.stdin = open('BOJ_2869.txt', 'r')

a,b,v = map(int,input().split())
k = 0
d = 0
while 1:
    k+=1
    if a*k-b*(k-1)>=v:
        break
print(k)