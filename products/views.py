from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Product
from utils.decorators import role_required

def home(request):
    featured_products = Product.objects.all()[:3]  # Get 3 featured products
    return render(request, 'products/home.html', {
        'products': featured_products
    })

@role_required(['admin', 'staff'])
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'products/product_detail.html', context)
    

