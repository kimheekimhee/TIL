def solution(x):
    answer = True
    n_sum = 0
    x = str(x)
    n_list = list(map(int, x))
    for i in n_list:
        n_sum += int(i)
    x = int(x)
    if x % n_sum == 0:
        answer = True
    else:
        answer = False
    return answer