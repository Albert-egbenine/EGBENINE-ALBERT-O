from django import forms
from django.contrib.auth.models import User
from .models import Booking

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('tickets',)
        widgets = {
            'tickets': forms.NumberInput(attrs={'min': 1, 'value': 1})
        }
