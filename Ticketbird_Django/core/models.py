from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('concert', 'Concert'),
        ('theater', 'Theater'),
        ('conference', 'Conference'),
        ('sports', 'Sports'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/')
    location = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    tickets = models.PositiveIntegerField(default=1)

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )
    payment_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True  # ✅ ensures Paystack transaction references are unique
    )

    def __str__(self):
        return f"{self.user.username} → {self.event.title} ({self.payment_status})"