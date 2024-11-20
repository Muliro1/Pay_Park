from django.shortcuts import render, redirect
from django.contrib.auth import login
from .authentication import CustomUserBackend
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    # Login view implementation
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUserBackend().authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    # Logout view implementation
    pass