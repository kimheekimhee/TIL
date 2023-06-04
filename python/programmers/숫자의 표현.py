def solution(n):
    count = 0                      
    for i in range(1, n+1):
        sum_n = 0                     
        for j in range(i, n+1):
            sum_n += j
            if sum_n == n:
                count += 1          
                break
            if sum_n > n:
                break
    return count