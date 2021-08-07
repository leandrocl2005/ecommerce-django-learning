from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/',
         views.category_list,
         name='category_list'),
    path('', views.product_list, name='products_list'),
]
