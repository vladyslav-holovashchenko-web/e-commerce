from django.shortcuts import render

products = [
    {
        "name": "Product 1",
        "price": 29.99,
        "image_url": "https://via.placeholder.com/300",
    },
    {
        "name": "Product 2",
        "price": 49.99,
        "image_url": "https://via.placeholder.com/300",
    },
    {
        "name": "Product 3",
        "price": 19.99,
        "image_url": "https://via.placeholder.com/300",
    },
    {
        "name": "Product 4",
        "price": 99.99,
        "image_url": "https://via.placeholder.com/300",
    },
    {
        "name": "Product 5",
        "price": 15.99,
        "image_url": "https://via.placeholder.com/300",
    },
]


def home(request):
    last_added_products = products
    return render(
        request, "shop/home.html", {"last_added_products": last_added_products}
    )
