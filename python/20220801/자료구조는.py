import sys

sys.stdin = open("자료구조는_input.txt")

stack = [11, 10, 8, 5]

comparison = stack.pop()

while len(stack) != 0:
    print(stack[-1], comparison)
    if stack[-1] > comparison:
        comparison = stack.pop()