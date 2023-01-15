def solution(array: list) -> int:
    dict = {}

    for num in array:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
            
    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)
    
    if len(result) <= 1:
        return result[0][0]
    return result[0][0] if result[0][-1] != result[1][-1] else -1