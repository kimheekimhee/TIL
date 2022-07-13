a, b = map(int, input().split(" "))

def rec(w, h):
    return w * h, (w + h) * 2

print(rec(a, b))