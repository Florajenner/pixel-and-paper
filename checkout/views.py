from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404, render
import stripe
from products.models import Product
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Please log in to make a purchase'}, status=403)
        
    product = get_object_or_404(Product, id=product_id)
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'unit_amount': int(product.price * 100),
                    'product_data': {
                        'name': product.title,
                        'description': product.description,
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/checkout/success/'),
            cancel_url=request.build_absolute_uri('/checkout/cancel/'),
            metadata={
                'product_id': product.id,
                'user_id': request.user.id
            }
        )

        # Create order
        Order.objects.create(
            user=request.user,
            product=product,
            stripe_pid=checkout_session.id
        )

        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def success_view(request):
    return render(request, 'checkout/success.html')

def cancel_view(request):
    return render(request, 'checkout/cancel.html')