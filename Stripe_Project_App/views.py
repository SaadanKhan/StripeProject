from django.shortcuts import render
from django.shortcuts import redirect
import stripe
from rest_framework.views import APIView
from .models import Product
from rest_framework import status
from rest_framework.response import Response


def ShowProducts(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


stripe.api_key = "Your Stripe Secret Key"
class StripePayment(APIView):
    def post(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': product.price*100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return redirect(session.url, code=303)


class Success(APIView):
    def get(self, request):
        message = "Thank you for paying"
        return render(request, 'message.html', {'message':message})


class Cancel(APIView):
    def get(self, request):
        message = "Error"
        return render(request, 'message.html', {'message':message})