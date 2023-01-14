def solution(numer1, denom1, numer2, denom2):
    # 1. 두 분수의 합 계산
    numer = denom1 * denom2
    denom = numer1 * denom2 + numer2 * denom1
    
    # 2. 최대공약수 계산
    start = max(denom, numer)
    GCD = 0
    
    for num in range(start, 0, -1):
        if denom % num == 0 and numer % num == 0:
            GCD = num
            break
    
    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [denom / GCD, numer / GCD]
    return answer