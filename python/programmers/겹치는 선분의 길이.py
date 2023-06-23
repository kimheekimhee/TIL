def solution(lines):
    answer = 0
    s_p = []
    f_p = []
    point_list = []
    answer_point_list = []
    for line in lines:
        s_p.append(line[0])
        f_p.append(line[1])
    for i in range(len(lines)):        
        for j in range(s_p[i], f_p[i]):
            point_list.append(j)
    # print(point_list)
    for p in point_list:
        if point_list.count(p) >= 2:
            answer_point_list.append(p)
    # print(len(set(answer_point_list)))
    answer = len(set(answer_point_list))
    return answer