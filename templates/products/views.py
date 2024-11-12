# products/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    """View for home page"""
    featured_products = Product.objects.all()[:3]  # Get first 3 products for featured section
    context = {
        'products': featured_products,
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    """View for product list page"""
    products = Product.objects.all()
    
    # Handle search queries
    query = request.GET.get('q')
    if query:
        products = products.filter(title__icontains=query)
    
    # Handle category filtering
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)
    
    context = {
        'products': products,
        'categories': Product.objects.values_list('category', flat=True).distinct()
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    """View for product detail page"""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)