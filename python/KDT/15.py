word = 'applaae'

locate = 0


for i in range(len(word)):
    if word[i] == 'a':
        break
    locate += 1
else:
    locate = '-1'

print (locate)

# 15(1)

result = []

for i in range(len(word)):
    if word[i] == 'a':
        result.append(i)
        print(i, end=' ')