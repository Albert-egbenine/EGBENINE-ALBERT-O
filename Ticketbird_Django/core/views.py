import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse
from .models import Event, Booking
from .forms import SignUpForm, BookingForm


def home(request):
    events = Event.objects.order_by('date')
    return render(request, 'core/home.html', {'events': events})


@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            # generate a fake reference
            booking.payment_reference = f"REF-{uuid.uuid4().hex[:10].upper()}"
            booking.save()
            # redirect to fake payment page
            return redirect(reverse('fake_payment', args=[booking.id]))
    else:
        form = BookingForm()
    return render(request, 'core/book_event.html', {'event': event, 'form': form})


@login_required
def fake_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    total_amount = booking.event.price * booking.tickets

    if request.method == "POST":
        if "pay_success" in request.POST:
            booking.payment_status = "successful"
            booking.save()
            return redirect("payment_success", booking_id=booking.id)
        elif "pay_fail" in request.POST:
            booking.payment_status = "failed"
            booking.save()
            return redirect("payment_failed", booking_id=booking.id)

    return render(request, "core/fake_payment.html", {"booking": booking, "total_amount": total_amount,})


@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, "core/payment_successful.html", {"booking": booking})


@login_required
def payment_failed(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, "core/payment_failed.html", {"booking": booking})


@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user).select_related('event').order_by('-booked_at')
    return render(request, 'core/dashboard.html', {'bookings': bookings})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/register.html', {'form': form})