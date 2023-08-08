import sys

sys.stdin = open("BOJ_2720.txt", "r")

T=int(input())
Qu=25
Di=10
Ni=5
Pe=1
for tc in range(1, T+1):
    C=int(input())
    #print(C)
    ans_Qu=C//Qu
    #print(ans_Qu)
    C2=C-Qu*ans_Qu
    #print(C2)
    ans_Di=C2//Di
    #print(ans_Di)
    C3=C2-Di*ans_Di
    #print(C3)
    ans_Ni=C3//Ni
    #print(ans_Ni)
    C4=C3-Ni*ans_Ni
    #print(C4)
    ans_Pe=C4//Pe
    #print(ans_Pe)
    print(ans_Qu, ans_Di, ans_Ni, ans_Pe)