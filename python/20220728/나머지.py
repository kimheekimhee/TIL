import sys

sys.stdin = open("나머지_input.txt")


count_ = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())
# print(a, b, c, d)
a_ = a % 42
b_ = b % 42
c_ = c % 42
d_ = d % 42
e_ = e % 42
f_ = f % 42
g_ = g % 42
h_ = h % 42
i_ = i % 42
j_ = j % 42

# print(a_, b_, c_)
list_ = [a_, b_, c_, d_, e_, f_, g_, h_, i_, j_]
# print(type(set(list_)))
for i in list(set(list_)):
    count_ += 1
print(count_)