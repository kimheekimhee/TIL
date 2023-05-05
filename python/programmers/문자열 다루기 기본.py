def solution(s):
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
    char_list = list(s)
    print(char_list)
    print(number_list)
    for char in char_list:
        if char not in number_list:
            return False
    len_list = [4, 6]
    if len(s) not in len_list:
        return False
    return True