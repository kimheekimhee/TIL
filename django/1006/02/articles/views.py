from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    # 글의 pk에 해당하는 db 값을 보내주기
    articles = Article.objects.get(pk=pk)
    context = {
        "articles": articles,
    }
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect("articles:index")


def update(request, pk):
    articles = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=articles)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", articles.pk)
    else:
        article_form = ArticleForm(instance=articles)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)
