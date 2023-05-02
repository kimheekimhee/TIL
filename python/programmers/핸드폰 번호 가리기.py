def solution(phone_number):
    answer = ''
    
    phone_number = list(str(phone_number))
    
    new_phone_number = []
    
    for _ in range(len(phone_number) - 4):
        new_phone_number.append('*')
        
    new_phone_number += phone_number[-4:]
    
    for i in new_phone_number:
        answer += i
        
    return answer