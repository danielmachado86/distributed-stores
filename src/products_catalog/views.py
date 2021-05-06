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
    return render(request, 'products_catalog/product_list.html', context)


def product_add_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente el producto: ' + request.POST['name'])
        form = ProductForm()
    else:
        for error in form.non_field_errors():
            messages.error(request, error)

    context = {
        'form': form
    }
    return render(request, 'products_catalog/product_add.html', context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    specs = ProductSpecs.objects.filter(product=obj.id)
    specs_form = ProductSpecsForm()
    if request.method == 'POST':
        specs_form = ProductSpecsForm(request.POST or None)
        if specs_form.is_valid():
            specs = specs_form.save(commit=False)
            specs.product = obj
            specs.save()
            messages.success(request, 'La especificación se añadio con exito')
            print(specs)
        return HttpResponseRedirect(request.path_info)

    context = {
        'object': obj,
        'specsForm': specs_form,
        'specs': specs
    }
    return render(request, 'products_catalog/product_detail.html', context)

def product_edit_view(request, id):
    obj = Product.objects.get(id=id)
    specs = ProductSpecs.objects.filter(product=obj.id)
    form = ProductForm(instance=obj)
    specs_form = ProductSpecsForm()
    if request.method == 'POST':
        if 'save_product_info' in request.POST:
            form = ProductForm(request.POST or None, instance=obj)
            if form.is_valid():
                print(form.is_valid())
                form.save()
                messages.success(request, 'El producto se actualizó exitosamente')
            else:
                print(form.errors)
                for error in form.non_field_errors():
                    messages.error(request, error)

        if 'save_product_specs' in request.POST:
            specs_form = ProductSpecsForm(request.POST or None)
            if specs_form.is_valid():
                specs = specs_form.save(commit=False)
                specs.product = obj
                specs.save()
                messages.success(request, 'La especificación se añadio con exito')

    context = {
        'form': form,
        'specsForm': specs_form,
        'specs': specs
    }
    return render(request, 'products_catalog/product_edit.html', context)


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


def brand_list_view(request):
    obj = Brand.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/brand_list.html', context)


def brand_add_view(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente la marca: ' + request.POST['name'])
        form = BrandForm()

    context = {
        'form': form
    }
    return render(request, 'products_catalog/brand_add.html', context)


def brand_edit_view(request, id):
    obj = Brand.objects.get(id=id)
    form = BrandForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'La marca se actualizó exitosamente')
    context = {
        'form': form
    }
    return render(request, 'products_catalog/brand_edit.html', context)


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


def category_list_view(request):
    obj = Category.objects.all()
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/category_list.html', context)


def category_add_view(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Se creó exitosamente la categoria: ' + request.POST['name'])
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'products_catalog/category_add.html', context)


def category_edit_view(request, id):
    obj = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'La categoria se actualizó exitosamente')
    context = {
        'form': form
    }
    return render(request, 'products_catalog/category_edit.html', context)


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