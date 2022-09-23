from django.shortcuts import render
import random
# Create your views here.
# HTTP : 요청(request)을 하면 무언가를 응답(response)하는 방식
# index 함수 선언  정의
def index(request):

    return render(request, "index.html")

def template(request):
    _number = 1
    context = {
        "number" : _number
    }
    return render(request, "template.html", context)

def dinner(request):
    dinner_list = [
        {"name": "살치살", "src": "https://t1.daumcdn.net/cfile/tistory/2229D04B5456209E28"},
        {"name": "등심", "src": "https://cdn.banhanu.com/images/1000000065_1.jpg"}
    ]

    context = {
        "dinner" : random.choice(dinner_list)
    }
    return render(request, "dinner.html", context)

def lotto(request):
    random.sample(range[1, 46], 6)
    lotto_list.append(lotto)
    context = {
        "lotto" == lotto,
    }

    return render(request, "lotto.html")