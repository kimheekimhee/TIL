word = 'banana'

result = ''

for i in word:
    # 1. 알파벳을 숫자로 바꾸고

    # 2. 숫자를 -32 하고

    # 3. 숫자를 알파벳으로 바꾼다.

    print(ord(i))

    number = ord(i)

    number_2 = number - 32

    print(chr(number_2))

    result += chr(number_2)