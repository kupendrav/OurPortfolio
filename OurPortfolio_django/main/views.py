from django.shortcuts import render
# Importing database to display name
from .models import Portfolio

# Create your views here.
def index(request):
    # user = Portfolio.objects.get(user_name=user_name)
    return render(request, "portfolio1/home.html")

def portfolios(request, id):
    user = Portfolio.objects.get(id=id)
    return render(request, "portfolio1/portfolios1.html", {
        "user": user
    })

def portfolios_username(request, username):
    user = Portfolio.objects.get(user_name=username)
    return render(request, "portfolio1/portfolios1.html", {
        "user": user
    })