from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .authentication import CustomUserBackend
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate
from django.utils import timezone
from .forms import ReserveParkingForm
from reservations.models import ParkingReservation, ParkingSlip
from parking.models import ParkingSlot, ParkingLot
from customers.models import Customer


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password, email=email)
            #Customer.objects.create(user=user, vehicle_number='', registration_date=timezone.now(), is_regular_customer=False, contact_number='')
            login(request, user)
            return redirect('login')
    
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    error_message = None
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Please enter both username and password'
    return render(request, 'users/login.html', {'form': form, 'error': error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


def home_view(request):
    return render(request, 'users/home.html')
@login_required
def reserve_parking(request):
    if request.method == 'POST':
        form = ReserveParkingForm(request.POST)
        if form.is_valid():
            parking_slot = form.cleaned_data['parking_slot']
            parking_lot = form.cleaned_data['parking_lot']
            start_timestamp = form.cleaned_data['start_timestamp']
            duration_in_minutes = form.cleaned_data['duration_in_minutes']
            booking_date = form.cleaned_data['booking_date']
            
            # Create the ParkingReservation instance
            reservation = ParkingReservation.objects.create(
                customer=request.user.customer,
                start_timestamp=start_timestamp,
                duration_in_minutes=duration_in_minutes,
                booking_date=booking_date,
                parking_slot=parking_slot,
                #parking_lot=parking_lot
            )
            slip_number = f"SLIP-{reservation.id}"
            ParkingSlip.objects.create(
                reservation=reservation,
                #slip_number=slip_number
            )
            return redirect('reserve_parking')
    else:
        form = ReserveParkingForm()
    return render(request, 'users/reserve_parking.html', {'form': form})

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')