import sys

sys.stdin = open("성적 통계_input.txt")

K = int(input())

for test_case in range(1, K + 1):
    G = list(map(int, input().split()))
    del G[0] # 첫번째 수([0])는 학생수이므로 계산에 필요없음
    G_ = sorted(G)
    gap_list_ = []
    print(G_)
    print(range(len(G_)), range(len(G_)-1))
    for _ in range(len(G) - 1):
        gap = G_[_ + 1] - G_[_]
        gap_list_.append(gap)
    print(f'Class {test_case}')
    print(f'Max {max(G)},', f'Min {min(G)},', f'Largest gap {max(gap_list_)}')