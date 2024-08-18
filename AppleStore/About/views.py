from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from About.serializers import CategorySerializer, ParametrSerializer, ProductSerializer, ProductSerializerSimple, TagSerializer
from basket.forms import BasketAddProductForm
from .models import *
from .forms import *

def redirectToProductPage(request):
    return redirect('product_page')


class AppleList(ListView):
    model = Product
    template_name = 'About/product/all_product.html'
    allow_empty = True
    

def detail_product(request, pk):
    model = get_object_or_404(Product, pk=pk)
    context = {
        'object': model,
        'form_basket': BasketAddProductForm 
    }
    return render(request, 'About/product/one_product.html', context)
    

class AppleCreate(CreateView):
    model = Product
    template_name = 'About/product/product_form.html'
    extra_context = {
        'action': 'Create product'
    }
    form_class = ProductForm
    

class AppleUpdate(UpdateView):
    model = Product
    template_name = 'About/product/product_form.html'
    extra_context = {
        'action': 'Update product'
    }
    form_class = ProductForm
    

class AppleDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_page')
    

class SupplierList(ListView):
    model = Supplier
    template_name = 'About/supplier/all_supplier.html'
    allow_empty = True


class SupplierDetail(DeleteView):
    model = Supplier
    template_name = 'About/supplier/detail_supplier.html'
    

class SupplierCreate(CreateView):
    model = Supplier
    template_name = 'About/supplier/supplier_form.html'
    extra_context = {
        'action': 'Create supplier'
    }
    form_class = SupplierForm
    

class SupplierUpdate(UpdateView):
    model = Supplier
    template_name = 'About/supplier/supplier_form.html'
    extra_context = {
        'action': 'Update supplier'
    }
    form_class = SupplierForm
    

class SupplierDelete(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier_page')
    

class OrderList(ListView):
    model = PosOrder
    template_name = 'About/order/all_order.html'
    allow_empty = True
    

class OrderDetail(DetailView):
    model = PosOrder
    template_name = 'About/order/detail_order.html'
    

class DeleteOrder(DeleteView):
    model = PosOrder
    success_url = reverse_lazy('order_page')


def test_json(request):
    return JsonResponse({
        'message': 'Данные в виде JSON',
        'products': reverse_lazy('product_page'),
        'suppliers': reverse_lazy('supplier_page')
    })
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSetDif(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductSerializer
        return ProductSerializerSimple
    
class ParametrViewSet(viewsets.ModelViewSet):
    queryset = Parametr.objects.all()
    serializer_class = ParametrSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class PaginationPage(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 1


class ProductPaginationViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationPage

