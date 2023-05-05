def solution(price, money, count):
    answer = 0
    real_price = 0
    for i in range(1, count+1):
        real_price += i*price
    answer = real_price - money
    if answer < 0:
        answer = 0
    return answer