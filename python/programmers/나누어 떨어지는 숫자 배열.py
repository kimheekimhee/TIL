def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        else:
            continue
    answer = sorted(answer)
    if len(answer) == 0:
        answer.append(-1)
    return answer