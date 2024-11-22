from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from .models import Cart, CartItem
from products.models import Product
from decimal import Decimal

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_key)
    return cart

@ensure_csrf_cookie
def cart_view(request):
    cart = get_or_create_cart(request)
    context = {
        'cart': cart,
        'cart_items': cart.items.select_related('product').all(),
        'total': cart.get_total(),
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                raise ValueError("Quantity must be positive")
            
            product = get_object_or_404(Product, id=product_id)
            cart = get_or_create_cart(request)
            
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            messages.success(request, f"{product.title} added to cart.")
            return redirect('cart_view')
            
        except (ValueError, TypeError) as e:
            messages.error(request, "Invalid quantity specified.")
        except Product.DoesNotExist:
            messages.error(request, "Product not found.")
        except Exception as e:
            messages.error(request, "Error adding item to cart.")
            
    return redirect('cart_view')

def update_cart(request, item_id):
    if request.method == 'POST':
        try:
            cart_item = get_object_or_404(CartItem, id=item_id)
            quantity = int(request.POST.get('quantity', 0))
            
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
                
            cart = cart_item.cart
            subtotal = float(cart_item.get_subtotal())
            cart_total = float(cart.get_total())
            
            return JsonResponse({
                'subtotal': subtotal,
                'cart_total': cart_total,
                'item_count': cart.get_item_count()
            })
            
        except (CartItem.DoesNotExist, ValueError, TypeError):
            return JsonResponse({'error': 'Invalid request'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Invalid method'}, status=405)

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        try:
            cart_item = get_object_or_404(CartItem, id=item_id)
            cart_item.delete()
            messages.success(request, "Item removed from cart.")
        except CartItem.DoesNotExist:
            messages.error(request, "Item not found.")
        except Exception:
            messages.error(request, "Error removing item from cart.")
            
    return redirect('cart_view')