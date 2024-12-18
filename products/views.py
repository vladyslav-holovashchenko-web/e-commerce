from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from cart.models import CartItem
from .forms import ProductForm, OrderForm


def add_product(request):
    """View to add a new product."""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


def product_list(request):
    """View to display the list of products."""
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    """View to display a single product and handle adding to the cart."""
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                defaults={"quantity": form.cleaned_data["quantity"]},
            )

            if not created:
                cart_item.quantity += form.cleaned_data["quantity"]
                cart_item.save()

            return redirect("product_list")
    else:
        form = OrderForm()

    return render(
        request,
        "products/product_detail.html",
        {"product": product, "form": form},
    )
