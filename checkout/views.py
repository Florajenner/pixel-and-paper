from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, product_id=None):
    try:
        line_items = []
        
        if product_id:
            # Single product checkout
            product = get_object_or_404(Product, id=product_id)
            line_items.append({
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.title,
                        'description': product.description,
                    },
                },
                'quantity': 1,
            })
        else:
            # Cart checkout
            cart = request.cart
            for item in cart.items.all():
                line_items.append({
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': int(item.product.price * 100),
                        'product_data': {
                            'name': item.product.title,
                            'description': item.product.description,
                        },
                    },
                    'quantity': item.quantity,
                })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def success_view(request):
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')