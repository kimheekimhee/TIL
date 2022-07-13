str = 'apple'
str_reverse = ''
for char in str:
    str_reverse = char + str_reverse

print(str_reverse)

word = 'apple'

for char in range ( len ( word ) ) :
    print(word[len(word)-char-1], end = '')