from django.shortcuts import render

# Create your views here.
def index(request, number_):
    if int(number_) == 0:
        result_ = "0"
    elif int(number_) % 2 == 0:
        result_ = "짝수"
    elif int(number_) % 2 == 1:
        result_ = "홀수"

    context = {
        "number_": number_,
        "result_": result_,
    }
    return render(request, "oddeven/index.html", context)
