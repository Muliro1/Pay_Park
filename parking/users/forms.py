from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import timedelta
from reservations.models import ParkingSlip

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields  = ['username', 'email', 'password', 'password_confirm']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        # Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        email = cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists!")
        return cleaned_data
    
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        return cleaned_data

class ReserveParkingForm(forms.Form):
    start_timestamp = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    duration_in_minutes = forms.IntegerField()
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    parking_slot = forms.ModelChoiceField(queryset=ParkingSlip.objects.all())


    def clean(self):
        cleaned_data = super().clean()
        start_timestamp = cleaned_data.get('start_timestamp')
        duration_in_minutes = cleaned_data.get('duration_in_minutes')
        booking_date = cleaned_data.get('booking_date')
        

        if start_timestamp and duration_in_minutes:
            end_timestamp = start_timestamp + timedelta(minutes=duration_in_minutes)
            if end_timestamp < timezone.now():
                raise ValidationError("The reservation end time must be in the future.")

        return cleaned_data
    