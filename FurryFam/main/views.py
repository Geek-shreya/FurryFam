from django.shortcuts import render
from django.http import HttpResponse
from .models import Login,Product
from math import ceil

def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nslides), nslides])
    params = { 'allProds' : allProds}
    return render(request, 'main/index.html', params)


def login(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        login = Login(name=name, email=email, phone=phone)
        login.save()
        return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')



def about(request):
    return render(request, 'main/about.html')


