from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout


def user_registraion(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                print(user)
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('product_page')
            messages.error(request, 'Данные введены не верно!')
        else:
            form = UserRegistration()
        return render(request, 'Profile/reg.html', context={'form': form})
    else:
        return redirect('product_page')


def user_login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, 'You success auth!')
                return redirect('product_page')
            messages.error(request, 'Woops, data filled wrong')
        else:
            form = LoginForm()
            return render(request, 'Profile/login.html', {'form': form})
    else:
        return redirect('product_page')
    


def user_logout(request):
    logout(request)
    messages.success(request, 'You came out from a profile!')
    return redirect('product_page')