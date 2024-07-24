from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpRequest
# Create your views here.

def register_view(request: HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })


def login_view(request: HttpRequest):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('posts:list')
        else:
            render(request, 'users/login.html', { 'form': form })

    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })


def logout_view(request:HttpRequest):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')