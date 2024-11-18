from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
import traceback
from django.core.mail.backends.smtp import EmailBackend

def test_email(request):
    try:
        # Create a custom email backend with specific local address
        connection = EmailBackend(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
            fail_silently=False,
            timeout=30,
            local_hostname='localhost'  # Specify local hostname
        )
        
        # Send email using this connection
        send_mail(
            subject='Test Email',
            message='This is a test email from your Django app.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            connection=connection,
            fail_silently=False,
        )
        return HttpResponse('Test email sent successfully!')
    except Exception as e:
        error_trace = traceback.format_exc()
        return HttpResponse(f'Error sending email:\n{str(e)}\n\nTraceback:\n{error_trace}')