from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('', redirectToProductPage),
    
    path('product/all', AppleList.as_view(), name="product_page"),
    path('product/<int:pk>', detail_product, name="one_product"),
    path('product/create', AppleCreate.as_view(), name="create_product"),
    path('product/update/<int:pk>', AppleUpdate.as_view(), name="update_product"),
    path('product/delete/<int:pk>', AppleDelete.as_view(), name="delete_product"),
    
    path('supplier/all', SupplierList.as_view(), name="supplier_page"),
    path('supplier/<int:pk>', SupplierDetail.as_view(), name="supplier_detail"),
    path('supplier/create', SupplierCreate.as_view(), name="create_supplier"),
    path('supplier/update/<int:pk>', SupplierUpdate.as_view(), name="update_supplier"),
    path('supplier/delete/<int:pk>', SupplierDelete.as_view(), name="delete_supplier"),
    
    path('order/all', OrderList.as_view(), name="order_page"),
    path('order/<int:pk>', OrderDetail.as_view(), name="order_detail"),
    path('order/delete/<int:pk>', DeleteOrder.as_view(), name="order_delete"),
]

router = routers.SimpleRouter()
router.register('api/products', ProductViewSet, basename='product')
router.register('api/product_simple', ProductViewSetDif, basename='product_simple')
router.register('api/parametr', ParametrViewSet, basename='parametr')
router.register('api/tag', TagViewSet, basename='tag')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/product_pagination', ProductPaginationViewSet, basename='product_pagination')
urlpatterns += router.urls

