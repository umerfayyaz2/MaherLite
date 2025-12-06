from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_bookings, name='bookings_home'),
    path('<int:service_id>/book/', views.create_booking, name='create_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
