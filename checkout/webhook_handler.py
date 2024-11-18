from django.http import HttpResponse
from orders.models import Order
import stripe
import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook"""
        intent = event.data.object
        pid = intent.id
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)

        # Update order
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(stripe_pid=pid)
                order.is_paid = True
                order.save()
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order already in database',
                status=200)
        else:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Order not found',
                status=500)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Payment Failed',
            status=200)