from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_http_methods(["POST"])
def create_checkout_session(request):
    try:
        cart = request.cart
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

        print("Line items:", line_items)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
        )

        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        print(f"Stripe error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)

def success_view(request):
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')