from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product, Brand, ProductSpecs
from .forms import CategoryForm, ProductForm, BrandForm, ProductSpecsForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def product_list_view(request):
    obj = Product.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente el producto: ' + request.POST['name'])
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products_catalog/product_create.html', context)


def product_update_view(request, id):
    obj = Product.objects.get(id=id)
    specs = ProductSpecs.objects.filter(product=obj.id)
    form = ProductForm(instance=obj)
    specs_form = ProductSpecsForm()
    if request.method == 'POST':
        if 'save_product_info' in request.POST:
            form = ProductForm(request.POST or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'El producto se actualizó exitosamente')
        if 'save_product_specs' in request.POST:
            specs_form = ProductSpecsForm(request.POST or None)
            if specs_form.is_valid():
                specs = specs_form.save(commit=False)
                specs.product = obj
                specs.save()
                messages.success(request, 'La especificación se añadio con exito')
        return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
        'specsForm': specs_form,
        'specs': specs
    }
    return render(request, 'products_catalog/product_update.html', context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Se eliminó exitosamente el producto: ' + obj.name)
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/product_delete.html', context)

def product_spec_delete_view(request, product, attribute):
    queryset = ProductSpecs.objects.filter(product=product)
    obj = get_object_or_404(queryset, attribute=attribute)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Se eliminó exitosamente la especificacion: ' + obj.attribute)
        return redirect('../../../')
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/product_spec_delete.html', context)


def brand_detail_view(request):
    obj = Brand.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/brand_detail.html', context)


def brand_create_view(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente la marca: ' + request.POST['name'])
        form = BrandForm()

    context = {
        'form': form
    }
    return render(request, 'products_catalog/brand_create.html', context)


def brand_update_view(request, id):
    obj = Brand.objects.get(id=id)
    form = BrandForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'La marca se actualizó exitosamente')
    context = {
        'form': form
    }
    return render(request, 'products_catalog/brand_update.html', context)


def brand_delete_view(request, id):
    obj = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Se eliminó exitosamente la marca: ' + obj.name)
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/brand_delete.html', context)


def category_detail_view(request):
    obj = Category.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/category_detail.html', context)


def category_create_view(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente la categoria: ' + request.POST['name'])
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'products_catalog/category_create.html', context)


def category_update_view(request, id):
    obj = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'La categoria se actualizó exitosamente')
    context = {
        'form': form
    }
    return render(request, 'products_catalog/category_update.html', context)


def category_delete_view(request, id):
    obj = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Se eliminó exitosamente la categoria: ' + obj.name)
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/category_delete.html', context)