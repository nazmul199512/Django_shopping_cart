from django.urls import path

from .views import product_list

app_name = 'products'

urlpatterns = [
    path(r'', product_list, name='product-list')
]
