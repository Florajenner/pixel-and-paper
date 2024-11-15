from django.urls import path
from . import views
from . import webhooks

urlpatterns = [
    path('wh/', webhooks.webhook, name='webhook'),
]