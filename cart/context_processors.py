from .views import get_or_create_cart

def cart_context(request):
    cart = get_or_create_cart(request)
    return {
        'cart': cart,
        'cart_count': cart.get_item_count() if hasattr(cart, 'get_item_count') else 0
    }