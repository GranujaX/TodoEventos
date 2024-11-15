from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Hubo un error iniciando sesion"))
            return redirect('login_user')
    else:
        return render(request, 'autenticacion/login_user.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CreateUserForm()

    return render(request, 'autenticacion/register_user.html', {'form':form})