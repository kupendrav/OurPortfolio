from django.shortcuts import render
# Importing database to display name
from .models import Portfolio

# Create your views here.
def index(request):
    # user = Portfolio.objects.get(user_name=user_name)
    return render(request, "portfolio1/home1.html")

# def portfolios(request, id):
#     user = Portfolio.objects.get(id=id)
#     return render(request, "portfolio1/portfolios1.html", {
#         "user": user
#     })

def portfolios_username(request, username):
    try:
        user = Portfolio.objects.get(user_name=username)
    except:
        print("something's not right")

    if user.porfolioTemplate == "BLUE":
        return render(request, "portfolio1/portfolio3.html", {
        "user": user
        })
    elif user.porfolioTemplate == "CREAM":
        return render(request, "portfolio1/portfolio2.html", {
        "user": user
        })
    elif user.porfolioTemplate == "DARK":
        return render(request, "portfolio1/portfolio4.html", {
        "user": user
        })
    else:
        return render(request, "portfolio1/portfolio1.html", {
        "user": user
        })
    