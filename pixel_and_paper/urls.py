from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views
from marketing import views as marketing_views

urlpatterns = [
    path('', product_views.home, name='home'),
    path('products/', include('products.urls')),
    path('marketing/', include('marketing.urls')),
    path('checkout/', include('checkout.urls')),  # Add this line
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)