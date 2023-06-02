def solution(food):
    answer = ''
    
    num = ''
    
    food_list = []
    
    for i in range(len(food)):
        food_list.append(f"{i}"*(food[i]//2))
    
    for n in food_list:
        num += n
    
    answer = num + '0' + num[::-1]
    
    return answer