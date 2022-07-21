import sys
sys.stdin = open('SWEA_1288_input.txt', 'r')

# T = int(input())

# for x in range(1, T + 1):

#     N = int(input())
#     count = 0
#     zero_to_nine = [str(i) for i in range(10)]

#     while zero_to_nine:

#         count += 1
#         room = N * count
#         room = str(room)

#         for c in room:
#             if c in zero_to_nine:
#                 zero_to_nine.remove(c)
#     print(f'#{x}', room)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N1 = N
    numbers = set()
    while len(numbers) < 10:
        for n in str(N):
            numbers.add(n)
        
        N += N1
        print(N)