from django.shortcuts import render
from .models import Order, CartItem


def order_list(request):
    """View to display all orders."""
    orders = Order.objects.all()
    return render(request, "orders/order_list.html", {"orders": orders})


def create_order(user):
    """Create an order for a given user."""
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items.exists():
        raise ValueError("No items in the cart to create an order.")

    order = Order.objects.create(user=user)

    order.items.set(cart_items)

    order.total_price = sum(item.quantity * item.product.price for item in cart_items)
    order.save()

    cart_items.delete()

    return order
