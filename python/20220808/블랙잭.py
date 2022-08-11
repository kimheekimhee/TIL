import sys

sys.stdin = open("블랙잭_input.txt")

N, M = map(int, input().split())
card = list(map(int, input().split()))

res = 0  # 결과값 초기화
# for 문 돌면서 비교검사
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] <= M:
                res = max(res, card[i] + card[j] + card[k])
print(res)