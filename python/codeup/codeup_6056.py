a, b = map(int, input().split())

i = bool(a)
j = bool(b)

print(i and (not j)) or ((not i) and j)