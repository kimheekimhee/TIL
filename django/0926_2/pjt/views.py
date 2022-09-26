from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, "index.html")


def is_odd_even(request, _number):
    context = {"number": _number}
    return render(request, "is_odd_even.html", context)


def random_game(request):

    return render(request, "random_game.html")
