from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from About.models import Product, PosOrder, Order
from .basket import Basket
from .forms import *


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            reload_count=form.cleaned_data['reload']
        )
    return redirect('basket_detail')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('product_list_filter')

    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(buyer_lastname=form.cleaned_data['buyer_lastname'],
                                     buyer_name=form.cleaned_data['buyer_name'],
                                     buyer_surname=form.cleaned_data['buyer_surname'],
                                     comment=form.cleaned_data['comment'],
                                     delivery=form.cleaned_data['delivery'],
                                     location=form.cleaned_data['location'])
        order.price = basket.get_total_price()
        for item in basket:
            posorder = PosOrder.objects.create(
                product=item['product'],
                count=item['count'],
                order=order
            )
        basket.clear()
    return redirect('basket_detail')


@login_required
def open_order(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'order/order_form.html', context)
