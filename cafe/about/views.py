from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import *


def catalog_list(request):
    model = Product.objects.filter(is_exists = False)
    context = {
        'dish_list': model
    }
    return render(request, 'cafe/main/index.html', context)


def dish(request, id):
    model = get_object_or_404(Product, pk=id)
    context = {
        'dish': model
    }
    return render(request, 'cafe/dish/dish.html', context)


@login_required()
def order_dish(request):
    messages.success(request, 'Товар был успешно заказан!')
    return redirect('catalog_dish_page')


def all_supplier(request):
    model = Supplier.objects.filter(is_exists = False)
    context = {
        'all_supplier': model
    }
    return render(request, 'cafe/supplier/main/all.html', context)
    

def add_product(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form_add_product = ProductForm(request.POST)
            if form_add_product.is_valid():
                new_product = Product(**form_add_product.cleaned_data)
                new_product.save()
                messages.success(request, 'Товар был успешно добавлен!')
                return redirect('catalog_dish_page')
            messages.error(request, 'Данные заполнены не верно!')
            return render(request, 'cafe/add/add_product.html', {'form': SupplierForm})
        else:
            form = ProductForm
            context = {
                'form': form
            }
            return render(request, 'cafe/add/add_product.html', context)
    else:
        messages.error(request, 'Вы не являетесь сотрудником!')
        return redirect('catalog_dish_page')


def user_registraion(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно!')
                return redirect('catalog_dish_page')
            messages.error(request, 'Данные введены не верно!')
            return render(request, 'cafe/auth/reg.html', context={'form': form})
        else:
            form = UserRegistration()
        return render(request, 'cafe/auth/reg.html', context={'form': form})
    else:
        messages.error(request, 'Вы уже авторизованы!')
        return redirect('catalog_dish_page')


def user_login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('catalog_dish_page')
            messages.error(request, 'Что-то заполнено не верно!')
            return redirect('log in')
        else:
            form = LoginForm()
            return render(request, 'cafe/auth/login.html', {'form': form})
    else:
        messages.error(request, 'Вы уже авторизованы!')
        return redirect('catalog_dish_page')
        

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта!')
    return redirect('catalog_dish_page')


class ListOrder(ListView):
    model = Order
    template_name = 'cafe/order/all.html'
    allow_empty = True
    

class DetailOrder(DeleteView):
    model = Order
    template_name = 'cafe/order/order.html'
    
    
class CreateOrder(CreateView):
    model = Order
    template_name = 'cafe/order/order_form.html'
    extra_context = {
        'action': 'Создать'
    }
    form_class = OrderCreateForm
    

class UpdateOrder(UpdateView):
    model = Order
    template_name = 'cafe/order/order_form.html'
    extra_context = {
        'action': 'Обновить'
    }
    form_class = OrderCreateForm
    

class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy('list_order')
    

class ListSupplier(ListView):
    model = Supplier
    template_name = 'cafe/supplier/main/all.html'
    allow_empty = True
    

class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'cafe/supplier/supplier/supplier.html'
    

class CreateSupplier(CreateView):
    model = Supplier
    template_name = 'cafe/supplier/supplier/supplier_form.html'
    extra_context = {
        'action': 'Добавить'
    }
    form_class = SupplierForm
    

class UpdateSupplier(UpdateView):
    model = Supplier
    template_name = 'cafe/supplier/supplier/supplier_form.html'
    extra_context = {
        'action': 'Обновить'
    }
    form_class = SupplierForm


class DeleteSupplier(DeleteView):
    model = Supplier
    success_url = reverse_lazy('all_supplier_list')
    

class ListSupply(ListView):
    model = PosSupply
    template_name = 'cafe/supply/all.html'
    allow_empty = True
    

class DetailSupply(DetailView):
    model = PosSupply
    template_name = 'cafe/supply/supply.html'


class CreateSupply(CreateView):
    model = PosSupply
    extra_context = {
        'action': 'Добавить'
    }
    template_name = 'cafe/supply/supply_form.html'
    form_class = SupplyForm
    

class UpdateSupply(UpdateView):
    model = PosSupply
    extra_context = {
        'action': 'Обновить'
    }
    template_name = 'cafe/supply/supply_form.html'
    form_class = SupplyForm
    

class DeleteSupply(DeleteView):
    model = PosSupply
    success_url = reverse_lazy('all_supply')