import sys

sys.stdin = open("BOJ_1157.txt", "r")


s = input().upper()  # .upper << 대문자 변환
# print(s) << MISSISSIPI
word_list = list(set(s))  # 중복 알파벳 제거, 리스트에 하나씩
# print(word_list) << ['I', 'M', 'S', 'P']
count_list = [s.count(i) for i in word_list]  # 각 알파벳이 몇개있는지 카운트
# print(count_list) << [4, 1, 4, 1]


# print(max(count_list)) << 4
if count_list.count(max(count_list)) > 1:  # 가장 큰 횟수가 또 있는지(동일한 횟수) 확인
    print("?")
else:
    print(word_list[count_list.index(max(count_list))])
