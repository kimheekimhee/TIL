from django.shortcuts import render, redirect
from .models import Todo
import datetime

# Create your views here.
def index(request):
    data = Todo.objects.all()
    return render(request, "todo/index.html", {"data": data})


def detail(request, _id):
    data = Todo.objects.get(id=_id)

    return render(request, "todo/detail.html", {"data": data})


def write(request):
    _title = request.GET.get("title")
    _content = request.GET.get("content")

    Todo.objects.create(title=_title, content=_content)

    return redirect("todo:index")


def update(request, _id):
    target = Todo.objects.get(id=_id)

    target.title = request.GET.get("title")
    target.content = request.GET.get("content")
    target.updated_at = datetime.date.today()

    target.save()

    return redirect("todo:detail", _id)


def delete(request, _id):
    Todo.objects.get(id=_id).delete()

    return redirect("todo:index")
