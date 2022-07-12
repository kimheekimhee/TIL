numbers = [0, 20, 100]
min_num = 0
# 1. 반복
for n in numbers:
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if min_num > n:
        min_num = n
print(min_num)