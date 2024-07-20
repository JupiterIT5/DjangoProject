from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('all/', catalog_list, name='catalog_dish_page'),
    path('all/dish/order/', order_dish, name='ordering_dish'),
    path('all/dish/<int:id>/', dish, name='menu_dish'),
    path('supplier/', all_supplier, name='all_supplier_list'),
    path('supplier/<int:id>/', supplier, name='supplier_menu'),
    path('supplier/add/', add_supplier, name="add_new_supplier"),
    path('dish/add/', add_product, name='add_new_product'),
    path('reg/', user_registraion, name='registr'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),
    path('order/all/', ListOrder.as_view(), name='list_order'),
    path('order/one/<int:pk>/', DetailOrder.as_view(), name='one_order'),
    path('order/delete/<int:pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('order/create/', CreateOrder.as_view(), name='create_order'),
    path('order/update/<int:pk>', UpdateOrder.as_view(), name='update_order')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)