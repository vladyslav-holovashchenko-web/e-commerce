from django.shortcuts import render


def home(request):
    categories = [
        {"name": "Electronics"},
        {"name": "Books"},
        {"name": "Clothing"},
        {"name": "Sports"},
        {"name": "Toys"},
    ]
    last_added_products = [
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
    featured_products = last_added_products
    recently_viewed = last_added_products

    return render(
        request,
        "shop/home.html",
        {
            "last_added_products": last_added_products,
            "featured_products": featured_products,
            "recently_viewed": recently_viewed,
            "categories": categories,
        },
    )
