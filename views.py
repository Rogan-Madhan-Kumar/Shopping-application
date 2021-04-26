from django.shortcuts import get_object_or_404, render 

from .models import Classification, Product

def classifications(request):
    return {
        'classifications' : Classification.objects.all() 
    }


def all_products (request):
    products = Product.objects.all()
    return render(request,'shop/homepage.html', {'products': products })

def login_page(request):
    return render(request,'shop/account.html')

def pants_page(request):
    pants = Product.objects.filter(Classification_id=3)
    return render(request,'shop/homepage.html', {'products': pants })

def shirts_page(request):
    shirts = Product.objects.filter(Classification_id=1)
    return render(request,'shop/homepage.html', {'products': shirts })

def tshirts_page(request):
    tshirts = Product.objects.filter(Classification_id=2)
    return render(request,'shop/homepage.html', {'products': tshirts })

def sweaters_page(request):
    sweaters = Product.objects.filter(Classification_id=4)
    return render(request,'shop/homepage.html', {'products': sweaters })

def product_detail(request, slug):
    product = get_object_or_404(Product , slug=slug , in_stock=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def category_list(request,category_slug):
    category = get_object_or_404(category , slug = category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'shop/product/category.html', {'category': category, 'products': products})
