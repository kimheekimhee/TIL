def solution(n): # 78
    answer = 0
    bin_n = bin(n)[2:]
    while True:
        # print(bin_n) # 1001110
        n = n + 1
        # print(n) 79
        bin_n_2 = bin(n)[2:]
        # print(bin_n_2) # 1001111
        if bin_n.count('1') == bin_n_2.count('1'):
            answer += n
            break
        
    return answer