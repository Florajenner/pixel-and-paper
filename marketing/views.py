from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, 'Successfully subscribed to newsletter!')
        return redirect('home')


def test_email(request):
    send_mail(
        'Test Email',
        'This is a test email from your Django app.',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    return HttpResponse('Test email sent!')