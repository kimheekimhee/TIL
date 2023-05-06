def solution(d, budget):
    answer = 0
    
    budget_minus_list = []
    
    d.sort()
    
    # print(d)
    
    for i in range(len(d)):
        
        budget -= d[i]
        
        
        
        if budget < 0:
            break
            
        budget_minus_list.append(budget)
        
    answer += len(budget_minus_list)
        
    return answer