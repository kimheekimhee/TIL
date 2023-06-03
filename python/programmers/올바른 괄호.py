def solution(s):
    s_list = []
    for i in s:
        if i == '(':
            s_list.append(i)
        else:            
            if s_list == []:
                return False
            else:
                s_list.pop()    
    if s_list != []:
        return False
    return True