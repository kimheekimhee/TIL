word = 'banana'

result = {}

for char in word:
    # 딕셔너리에 키가 없으면 ?
    if char not in result.keys():
        # 키랑 값을 1으로 초기화한다.
        result[char] = 1
    else:
        result[char] = result[char] + 1

print(result)

# 출력부분
for key in result:
    print(key,result[key])