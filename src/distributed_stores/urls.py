"""distributed_stores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products_catalog.views import (brand_create_view, brand_delete_view, 
    brand_detail_view, brand_update_view, category_create_view, category_delete_view, 
    category_detail_view, category_update_view, product_create_view, product_update_view, 
    product_list_view, product_delete_view, product_spec_delete_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list_view, name='product-list'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:id>/', product_update_view, name='product-update'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:product>/specs/<str:attribute>/delete/', product_spec_delete_view, name='product-spec-delete'),
    path('brands/', brand_detail_view, name='brand-list'),
    path('brands/create/', brand_create_view, name='brand-create'),
    path('brands/<int:id>', brand_update_view, name='brand-update'),
    path('brands/<int:id>/delete/', brand_delete_view, name='brand-delete'),
    path('categories/', category_detail_view, name='category-list'),
    path('categories/create/', category_create_view, name='category-create'),
    path('categories/<int:id>', category_update_view, name='category-update'),
    path('categories/<int:id>/delete/', category_delete_view, name='category-delete'),
]
