import sys

sys.stdin = open("BOJ_7785.txt", "r")

N = int(input())
pe = {}

for _ in range(N):
  p, c = input().split()

  if c == 'enter':
    pe[p] = 'enter'
  else:
    if pe[p]:
      del pe[p]

for people in sorted(pe, reverse=True):
  print(people)