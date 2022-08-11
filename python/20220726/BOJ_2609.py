# https://www.acmicpc.net/problem/2609
import sys

sys.stdin = open("BOJ_2609_input.txt")

a, b = map(int, input().split())
 
def GCD_(a, b):
    while b != 0:
        remainder_ = a % b
        a = b
        b = remainder_
    return a

def LCM_(a, b):
    LCM__ = (a * b) / GCD_(a, b)
    return LCM__

print(GCD_(a, b))
print(int(LCM_(a, b)))