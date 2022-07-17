import json

# 파일을 열고
f = open('stocks.json', 'r', encoding = 'utf-8')
# json 을 파이썬 객체 형식으로 한다
kospi = json.load(f)
samsung = kospi['stocks'][0]
print(samsung, type(samsung))