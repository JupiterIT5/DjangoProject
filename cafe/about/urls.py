from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('all', catalog_list, name='catalog_dish_page'),
    path('all/dish/order', order_dish, name='ordering_dish'),
    path('all/dish/<int:id>', dish, name='menu_dish'),
    path('supplier', ListSupplier.as_view(), name='all_supplier_list'),
    path('supplier/<int:pk>', DetailSupplier.as_view(), name='supplier_menu'),
    path('supplier/add', CreateSupplier.as_view(), name="add_new_supplier"),
    path('supplier/delete/<int:pk>', DeleteSupplier.as_view(), name='delete_supplier'),
    path('supplier/update/<int:pk>', UpdateSupplier.as_view(), name='update_supplier'),
    path('dish/add', add_product, name='add_new_product'),
    path('reg', user_registraion, name='registr'),
    path('login', user_login, name='log in'),
    path('logout', user_logout, name='log out'),
    path('order/all', ListOrder.as_view(), name='list_order'),
    path('order/<int:pk>', DetailOrder.as_view(), name='one_order'),
    path('order/delete/<int:pk>', DeleteOrder.as_view(), name='delete_order'),
    path('order/create', CreateOrder.as_view(), name='create_order'),
    path('order/update/<int:pk>', UpdateOrder.as_view(), name='update_order'),
    path('supply/all', ListSupply.as_view(), name='all_supply'),
    path('supply/<int:pk>', DetailSupply.as_view(), name='detail_supply'),
    path('supply/create', CreateSupply.as_view(), name='create_supply'),
    path('supply/update/<int:pk>', UpdateSupply.as_view(), name='update_supply'),
    path('supply/delete/<int:pk>', DeleteSupply.as_view(), name='delete_supply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)