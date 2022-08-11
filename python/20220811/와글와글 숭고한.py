import sys

sys.stdin = open("와글와글 숭고한.txt")

S, K, H = map(int, input().split())
Univ = [S, K, H]
if S + K + H >= 100:
    print('OK')
else:
    if min(Univ) == S:
        print('Soongsil')
    elif min(Univ) == K:
        print('Korea')
    else:
        print('Hanyang')