def solution(n, arr1, arr2):
    answer = []
    
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # bin(x) : x를 2진수로 변환
        # or = | , xor = ^ , and = &
        # arr1[i], arr2[i] 중 하나라도 1이라면 1, 따라서 or 연산
        # tmp결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n)
        # [2:] 2진수 변환시 앞 2자리의 2진수를 뜻하는 0b를 생략
        # x.zfill : 값이 없는 자리에 n자리수 만큼 0을 채움
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1','#').replace('0',' ')
        # 1을 #, 0을 공백 으로 변환
        # tmp결과 ex) ' ## #'
        answer.append(tmp)
    
    return answer