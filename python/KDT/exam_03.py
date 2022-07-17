import random


# 1 ~ 45 숫자 중 6개를 정렬해서 뽑기

n = int(input('얼마쓸래? '))
for i in range(n):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    print(numbers, type(numbers))