from django.shortcuts import render
from . models import Product
from . models import ProductCategory

# Create your views here.

def about(request):
    return render(request,'momos/aboutus.html')

def allergy(request):
    return render(request,'momos/allergy.html')

def services(request):
    return render(request,'momos/services.html')

def menu(request):
    categories = ProductCategory.objects.all()
    data = {}
    for category in categories:
        momos = category.product_set.all()
        data[category]=momos
        print(data)
    menu = Product.objects.all()
    return render(request,'momos/menu.html',{'data':data})
    # menus=Product.objects.all()
    # return render(request,'momos/menu.html',{'menus':menus})

def contact(request):
    return render(request,'momos/contact.html')

def home(request):
    return render(request,'momos/home.html')

