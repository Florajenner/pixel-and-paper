# cart/context_processors.py
from .views import get_or_create_cart

def cart_context(request):
    return {'cart': get_or_create_cart(request)}