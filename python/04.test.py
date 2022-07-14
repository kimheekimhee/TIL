word = 'kiwi'

locate = 0

for i in range(len(word)):
    if word[i] == 'a':
        break
    locate += 1
else:
    locate = '-1'

print (locate)
print(len(word))