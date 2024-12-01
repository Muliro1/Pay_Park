from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .authentication import CustomUserBackend
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate
from customers.models import Customer
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password, email=email)
            Customer.objects.create(user=user, vehicle_number='', registration_date=timezone.now(), is_regular_customer=False, contact_number='')
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

@login_required
def home_view(request):
    return render(request, 'users/home.html')
@login_required
def reserve_parking(request):
    return render(request, 'users/reserve_parking.html')

class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')