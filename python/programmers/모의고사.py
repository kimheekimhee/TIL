def solution(answers):
    answer = []
    n_1 = [1, 2, 3, 4, 5]
    n_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10
        
        if n_1[a1] == answers[i]:
            c1 += 1
        if n_2[a2] == answers[i]:
            c2 += 1
        if n_3[a3] == answers[i]:
            c3 += 1
            
    k = max(c1, c2, c3)
    
    if k == c1:
        answer.append(1)
    if k == c2:
        answer.append(2)
    if k == c3:
        answer.append(3)
    return answer