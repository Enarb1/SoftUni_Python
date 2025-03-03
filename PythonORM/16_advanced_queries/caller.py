import os
import django
from django.db.models import Count, Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
def product_quantity_ordered():
    result = []
    orders = Product.objects.annotate(
        total=Sum('orderproduct__quantity')
    ).values('name','total').order_by('-total').exclude(total=0)

    for o in orders:
        result.append(f"Quantity ordered of {o['name']}: {o['total']}")

    return "\n".join(result)


def ordered_products_per_customer():
    result = []
    orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name}, Category: {order_product.product.category.name}")

    return "\n".join(result)

def filter_products():
    result = []
    query = Q(is_available=True) & Q(price__gt=3.00)
    products = Product.objects.filter(query).order_by('-price', 'name')

    for product in products:
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)


def give_discount():
    result = []
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=F('price') * 0.7)
    products = Product.objects.filter(is_available=True).order_by('-price', 'name')

    for product in products:
        result.append(f"{product.name}: {product.price}lv.")

    return "\n".join(result)


# Run and print your queries

