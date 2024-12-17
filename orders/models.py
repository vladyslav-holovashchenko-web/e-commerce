from django.db import models
from users.models import CustomUser
from cart.models import CartItem
from decimal import Decimal


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending",
    )

    def calculate_total_price(self):
        """Calculate the total price based on the related cart items."""
        return sum(item.product.price * item.quantity for item in self.items.all())

    def save(self, *args, **kwargs):
        """Override save to update total_price before saving."""
        if not self.pk:  # Order does not yet exist
            super().save(*args, **kwargs)  # Save to get a primary key
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
