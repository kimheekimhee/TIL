def solution(a, b, n):
    # a = 주는 병 b = 받는 병 n = 가진 병
    answer = 0
    while n >= a:
        
        remain_bottle = n % a
        
        n = n // a * b
        
        answer += n
        
        n += remain_bottle
    
    return answer