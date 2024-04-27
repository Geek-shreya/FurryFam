import requests
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
        # email = request.POST.get('email', '')
        # phone = request.POST.get('phone', '')
        pss = request.POST.get('pss', '')
        # login = Login(name=name, email=email, pss=pss,phone=phone)
        login = Login(name=name, pss=pss)
        login.save()
        return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')



def about(request):
    return render(request, 'main/about.html')

def call(request):
    response = requests.get('https://api.example.com/data')
    
    if response.status_code == 200:
        data = response.json()
        return render(request, 'template.html', {'data': data})
    else:
        # Handle errors
        return HttpResponse("Error: Failed to fetch data from the API", status=response.status_code)


