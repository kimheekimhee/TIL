def solution(left, right):
    answer = 0
    range_list = []
    for i in range(left, right+1):
        range_list.append(i)
    
    for j in range_list:
        p_list = []
        for p in range(1, j+1):
            p_list.append(p)
        pp_list = []
        for pp in p_list:
            if j % pp == 0:
                pp_list.append(pp)
        if len(pp_list) % 2 == 0:
            j = j
        if len(pp_list) % 2 == 1:
            j = -j
        answer += j
    return answer