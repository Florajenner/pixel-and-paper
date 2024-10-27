from django.shortcuts import render, get_object_or_404
from .models import Product

# Home view
def home(request):
    return render(request, 'products/home.html')

# Product listing view
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Product detail view
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
