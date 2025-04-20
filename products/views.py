from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.
def index(request):
    user = "tom"
    product_num = 4
    products = Product.objects.all().order_by('id')[:4]
    return render(request, "products/home.html",{
        "name": user,
        "products_numb": product_num,
        "products": products,
    })

def signup(request):
    return render(request,"products/signup.html")
    

def product_cat(request, product, productid):
    if (product == "dress" or product == "suit" or product=="shirt" or product=="shoes" ):
        return HttpResponse(f"Here is the list of out {product}")
    else:
        return HttpResponse('Page does not exist')