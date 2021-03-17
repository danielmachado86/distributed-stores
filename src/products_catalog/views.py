from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'products_catalog/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        print(obj.id)
        # form = ProductForm()

    context = {
        'form': form,
        'object': obj
    }
    return render(request, 'products_catalog/product_create.html', context)