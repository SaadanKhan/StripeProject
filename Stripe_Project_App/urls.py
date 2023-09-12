from django.urls import path
from .views import StripePayment, Success, Cancel
from . import views

urlpatterns = [
    path('stripe_payment/<int:pk>/', StripePayment.as_view(), name='stripe_payment'),
    path('my-products/', views.ShowProducts),
    path('success/', Success.as_view()),
    path('cancel/', Cancel.as_view()),
]