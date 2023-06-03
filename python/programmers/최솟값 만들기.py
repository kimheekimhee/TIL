def solution(A,B):
    answer = 0

    AA = sorted(A)
    BB = sorted(B)
    BB = BB[::-1]
    
    for i in range(len(AA)):
        answer += AA[i]*BB[i]

    return answer