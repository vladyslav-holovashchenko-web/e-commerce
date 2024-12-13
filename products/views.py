from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/add_product.html", {"form": form})


def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})
