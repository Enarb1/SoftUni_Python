import os
from decimal import Decimal

import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions


def populate_db():
    adam = Profile.objects.create(
        full_name="Adam Smith",
        email="adam.smith@example.com",
        phone_number="123456789",
        address="123 Main St, Springfield",
        is_active=True
    )

    susan = Profile.objects.create(
        full_name="Susan James",
        email="susan.james@example.com",
        phone_number="987654321",
        address="456 Elm St, Metropolis",
        is_active=True
    )

    # Create Products
    desk = Product.objects.create(
        name="Desk M",
        description="A medium-sized office desk",
        price=150.00,
        in_stock=10,
        is_available=True
    )

    display = Product.objects.create(
        name="Display DL",
        description="A 24-inch HD display",
        price=200.00,
        in_stock=5,
        is_available=True
    )

    printer = Product.objects.create(
        name="Printer Br PM",
        description="A high-speed printer",
        price=300.00,
        in_stock=3,
        is_available=True
    )

    # Create Orders
    order1 = Order.objects.create(
        profile=adam,
        total_price=350.00,
        is_completed=False
    )
    order1.products.set([desk, display])

    order2 = Order.objects.create(
        profile=adam,
        total_price=300.00,
        is_completed=True
    )
    order2.products.set([printer])

    order3 = Order.objects.create(
        profile=adam,
        total_price=650.00,
        is_completed=False
    )
    order3.products.set([desk, display, printer])

    order4 = Order.objects.create(
        profile=susan,
        total_price=450.00,
        is_completed=False
    )
    order4.products.set([desk, printer])



def get_profiles(search_string=None):

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    if search_string is None or not Profile.objects.filter(query).exists():
        return ""

    profiles = Profile.objects.filter(query).order_by("full_name")

    return "\n".join(f"Profile: {p.full_name}, "
                      f"email: {p.email}, "
                      f"phone number: {p.phone_number}, "
                      f"orders: {p.orders.count()}" for p in profiles)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    return "\n".join(f"Profile: {p.full_name}, orders: {p.orders.count()}"
                     for p in profiles)


def get_last_sold_products():
    last_order = Order.objects.order_by('-creation_date', 'products__name').first()

    if not last_order or not Order.objects.all().exists():
        return ""

    products = ", ".join(last_order.products.all().values_list('name', flat=True))

    return f"Last sold products: {products}"


def get_top_products():
    products = Product.objects.annotate(
        order_count=Count('orders')).filter(
        order_count__gt=0).order_by('-order_count', 'name')[:5]

    if not products:
        return ""

    result = ["Top products:"]

    for p in products:
        result.append(f"{p.name}, sold {p.order_count} times")

    return "\n".join(result)


def apply_discounts():
    updated_orders = Order.objects.annotate(
        products_count=Count('products')).filter(
        is_completed=False, products_count__gt=2).update(total_price=F("total_price") * 0.9)

    return f"Discount applied to {updated_orders} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if not order:
        return ""

    order.is_completed = True
    order.save()

    for product in order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    return f"Order has been completed!"
