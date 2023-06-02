def solution(s):
    answer = ''
    s_list = s.split()
    i_list = []
    # print(s_list)
    for i in s_list:
        # print(type(i))
        i = int(i)
        # print(type(i))
        i_list.append(i)
    print(i_list)
    
    answer = f'{min(i_list)} {max(i_list)}'
    return answer