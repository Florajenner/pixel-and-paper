from django.urls import path
from . import views, webhooks

urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('create-checkout-session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success_view, name='checkout_success'),
    path('cancel/', views.cancel_view, name='checkout_cancel'),
    path('wh/', webhooks.webhook, name='webhook'),
]