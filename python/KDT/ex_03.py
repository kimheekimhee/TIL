# numbers = input().split()
# print(sum(numbers))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'

numbers = map(int, input().split())
print(sum(numbers))