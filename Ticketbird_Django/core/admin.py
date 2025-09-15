from django.contrib import admin
from .models import Event, Booking

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'location', 'price')
    list_filter = ('category', 'date')
    search_fields = ('title', 'location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'tickets', 'booked_at')
    list_filter = ('booked_at',)
