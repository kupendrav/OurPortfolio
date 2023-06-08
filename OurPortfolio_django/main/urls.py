from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.portfolios, name="name"),
    path("<str:username>", views.portfolios_username, name="name")

]