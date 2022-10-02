from django.urls import path
from . import views

app_name = "oddeven"

urlpatterns = [
    path("index/<number_>", views.index, name="index"),
]
