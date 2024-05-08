from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    print("Print Welcome !")
    # return HttpResponse("<h1>Welcome user</h1>")
    return render(request, "home.html", {})

def product(request):
    # return HttpResponse("<h1>Products we sell</h1>")
    return render(request, "product.html", {})


def services(request):
    # return HttpResponse("<h1>Services we provide</h1>")
    return render(request, "services.html", {})

