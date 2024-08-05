from django.shortcuts import render, get_object_or_404
from .models import *


def home_page(request):
    return render(request, 'about/index.html')

def political_conf(request):
    return render(request, 'Documents/Политика-конфиденциальности.pdf')

def public_ofera(request):
    return render(request, 'Documents/Публичная-оферта.pdf')

def shop_list(request):
    return render(request, 'about/shop.html')

def knowledgebase_list(request):
    return render(request, 'about/knowledgebase.html')

def knowbase_list(request):
    return render(request, 'about/knowbase.html')

def blog_page(request):
    model = Post.objects.all()
    context = {
        'post_list': model
    }
    return render(request, 'about/blog.html', context)

def contact_page(request):
    return render(request, 'about/contacts.html')

def post_one(request, id):
    model = get_object_or_404(Post, pk=id)
    context = {
        'post': model
    }
    return render(request, 'about/post.html', context)