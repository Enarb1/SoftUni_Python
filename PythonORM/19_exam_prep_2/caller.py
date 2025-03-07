import decimal
import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions

def populate_db():
    profiles = [
        Profile(
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            address="123 Main St, City A",
            is_active=True
        ),
        Profile(
            full_name="Jane Smith",
            email="jane.smith@example.com",
            phone_number="0987654321",
            address="456 Oak Ave, City B",
            is_active=True
        ),
        Profile(
            full_name="Bob Johnson",
            email="bob.johnson@example.com",
            phone_number="5555555555",
            address="789 Pine Rd, City C",
            is_active=True
        )
    ]
    Profile.objects.bulk_create(profiles)

    products = [
        Product(
            name="Laptop",
            description="High-performance laptop with 16GB RAM",
            price=decimal.Decimal("999.99"),
            in_stock=10,
            is_available=True
        ),
        Product(
            name="Smartphone",
            description="Latest model with 5G capability",
            price=decimal.Decimal("599.50"),
            in_stock=15,
            is_available=True
        ),
        Product(
            name="Headphones",
            description="Noise-cancelling wireless headphones",
            price=decimal.Decimal("149.99"),
            in_stock=20,
            is_available=True
        ),
        Product(
            name="Mouse",
            description="Ergonomic wireless mouse",
            price=decimal.Decimal("29.99"),
            in_stock=25,
            is_available=True
        )
    ]
    Product.objects.bulk_create(products)

    profile1, profile2, profile3 = Profile.objects.order_by('id')[:3]
    product1, product2, product3, product4 = Product.objects.order_by('id')[:4]

    orders = [
        Order(
            profile=profile1,
            total_price=decimal.Decimal("999.99"),
            is_completed=False
        ),
        Order(
            profile=profile2,
            total_price=decimal.Decimal("749.49"),
            is_completed=True
        ),
        Order(
            profile=profile3,
            total_price=decimal.Decimal("1179.97"),
            is_completed=False
        )
    ]
    Order.objects.bulk_create(orders)

    order1, order2, order3 = Order.objects.order_by('id')[:3]

    order1.products.add(product1)
    order2.products.add(product2, product3)
    order3.products.add(product1, product2)


def get_profiles(search_string=None):

    if search_string is not None:
        query = (Q(full_name__icontains=search_string) |
                Q(email__icontains=search_string) |
                Q(phone_number__icontains=search_string))

        profiles = Profile.objects.filter(query).order_by('full_name')

        if not profiles.exists():
            return ""

        result = []

        for p in profiles:
            orders_count = p.orders.count()
            result.append(f"Profile: {p.full_name}, "
                        f"email: {p.email}, "
                        f"phone number: {p.phone_number}, "
                        f"orders: {orders_count}")

        return "\n".join(result)
    return ""

def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles.exists():
        return ""

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.orders.count()}")

    return "\n".join(result)

def get_last_sold_products():

    last_sold_products = Order.objects.prefetch_related('products').last()

    if last_sold_products is None or not last_sold_products.products.exists():
        return ""

    products = ", ".join(last_sold_products.products.order_by('name').values_list('name', flat=True))

    return f"Last sold products: {products}"

def get_top_products():
    top_products =  Product.objects.annotate(
        order_count=Count('order'),
    ).filter(
        order_count__gt=0
    ).order_by(
        '-order_count', 'name'
    )[:5]

    if not top_products.exists():
        return ""

    result = []
    for p in top_products:
        result.append(f"{p.name}, sold {p.order_count} times")

    return f"Top products:\n" + '\n'.join(result)

def apply_discounts():
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False,
    ).update(
        total_price=F('total_price') * 0.90,
    )

    return f"Discount applied to {updated_orders_count} orders."

def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()

    if not order:
        return ""

    for p in order.products.all():
        p.in_stock -= 1

        if p.in_stock <= 0:
            p.is_available = False

        p.save()
    """doing everything with one query"""
    # order.products.update(
    #     in_stock=F('in_stock') - 1,
    #     is_available=Case(
    #         When(in_stock=1, then=Value(False)),
    #         default=F('is_available'),
    #         output_field=BooleanField()
    #     )
    # )

    order.is_completed = True
    order.save()
    return "Order has been completed!"
