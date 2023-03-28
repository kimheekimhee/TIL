def solution(s):
    answer = ''
    new_list = s.split(' ') # ' ' 일 때 분리
    # print(new_list) ['try', 'hello', 'world']
    for word in new_list: # ' ' 을 기준으로 나누어진 word
        for char in range(len(word)): # word 길이 만큼의 한 글자씩
            if char % 2 == 0: # 2로 나누었을때 나머지가 0 일 떄 (짝수)
                answer += word[char].upper()
            else:
                answer += word[char].lower()
        answer += ' ' # 다시 word 사이 ' ' 넣기
        
    return answer[0:-1] # 끝에 ' ' 빼기