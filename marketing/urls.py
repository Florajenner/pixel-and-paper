from django.urls import path
from . import views

urlpatterns = [
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('test-email/', views.test_email, name='test_email'),
]