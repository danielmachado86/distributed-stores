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

from products_catalog.views import (brand_add_view, brand_delete_view, 
    brand_list_view, brand_edit_view, category_add_view, category_delete_view, 
    category_list_view, category_edit_view, product_add_view, product_detail_view, product_edit_view, 
    product_list_view, product_delete_view, product_spec_delete_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list_view, name='product-list'),
    path('products/add/', product_add_view, name='product-add'),
    path('products/<int:id>/', product_detail_view, name='product-detail'),
    path('products/<int:id>/edit/', product_edit_view, name='product-edit'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:product>/specs/<str:attribute>/delete/', product_spec_delete_view, name='product-spec-delete'),
    path('brands/', brand_list_view, name='brand-list'),
    path('brands/add/', brand_add_view, name='brand-add'),
    path('brands/<int:id>/', brand_edit_view, name='brand-edit'),
    path('brands/<int:id>/delete/', brand_delete_view, name='brand-delete'),
    path('categories/', category_list_view, name='category-list'),
    path('categories/add/', category_add_view, name='category-add'),
    path('categories/<int:id>/', category_edit_view, name='category-edit'),
    path('categories/<int:id>/delete/', category_delete_view, name='category-delete'),
]
