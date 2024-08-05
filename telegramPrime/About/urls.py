from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('shop', shop_list, name="shop_list"),
    path('knowledgebase', knowledgebase_list, name="knowledgebase_list"),
    path('knowbase', knowbase_list, name="knowbase_list"),
    path('blog', blog_page, name='blog_page'),
    path('blog/post/<int:id>', post_one, name="post_one"),
    path('contact', contact_page, name='contact_page'),
    path('Documents/Политика-конфиденциальности.pdf', political_conf, name="political_conf"),
    path('Documents/Публичная-оферта.pdf', public_ofera, name="public_ofera"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)