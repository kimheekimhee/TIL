import sys

sys.stdin = open("FBI.txt")

FBI_list_ = []
for _ in range(5):
    name = input()
    # print(name)
    if 'FBI' in name:
        FBI_list_.append(name)
        print(_ + 1, end = ' ')
        # print(FBI_list_)
        # print(len(FBI_list_))
if len(FBI_list_) == 0:
    print('HE GOT AWAY!')