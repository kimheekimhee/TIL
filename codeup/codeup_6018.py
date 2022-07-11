a = '1 2 3'
print(a.split())
# 문자열을 특정 단위로 나누어줌
numbers = a.split()
result = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
print(result)

a = '10:20'
numbers = a.split(':')
print(numbers)
print(numbers[0], numbers[1], sep = '^')