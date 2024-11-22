from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from cart.views import get_or_create_cart
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_http_methods(["POST"])
def create_checkout_session(request, product_id=None):
    try:
        cart = get_or_create_cart(request)
        
        if product_id:
            # Single product checkout
            product = Product.objects.get(id=product_id)
            line_items = [{
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(float(product.price) * 100),
                    'product_data': {
                        'name': product.title,
                        'description': str(product.description)[:500] if product.description else '',
                    },
                },
                'quantity': 1,
            }]
        else:
            # Cart checkout
            if not cart or not cart.items.exists():
                return JsonResponse({'error': 'Cart is empty'}, status=400)

            line_items = []
            for item in cart.items.all():
                line_items.append({
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': int(float(item.product.price) * 100),
                        'product_data': {
                            'name': item.product.title,
                            'description': str(item.product.description)[:500] if item.product.description else '',
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
            metadata={
                'cart_id': cart.id if not product_id else None,
                'product_id': product_id if product_id else None,
            }
        )

        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        print(f"Stripe error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)

def success_view(request):
    cart = get_or_create_cart(request)
    cart.items.all().delete()  # Clear the cart after successful purchase
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')