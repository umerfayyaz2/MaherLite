from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import Service
from .models import Booking
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_booking(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        booking = Booking.objects.create(user=request.user, service=service, date=date, time=time)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': service.name},
                    'unit_amount': int(service.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/bookings/payment-success/') + '?booking_id=' + str(booking.id),
            cancel_url=request.build_absolute_uri('/services/'),
        )
        return redirect(checkout_session.url)
    return render(request, 'bookings/booking_form.html', {'service': service})

@login_required
def payment_success(request):
    booking_id = request.GET.get('booking_id')
    booking = Booking.objects.get(id=booking_id)
    booking.is_paid = True
    booking.save()
    return render(request, 'bookings/payment_success.html', {'booking': booking})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
