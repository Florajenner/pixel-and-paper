from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views
from marketing import views as marketing_views
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', product_views.home, name='home'),
    path('products/', include('products.urls')),
    path('marketing/', include('marketing.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)