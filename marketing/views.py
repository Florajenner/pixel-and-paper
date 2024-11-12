from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, 'Successfully subscribed to newsletter!')
        return redirect('home')