flowers = input()  # Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus
qty = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOULLS_PRICE = 2.50

final_price = 0

if flowers == "Roses":
    final_price = qty * ROSES_PRICE
    if qty > 80:
        final_price *= 0.9
elif flowers == "Dahlias":
    final_price = qty * DAHLIAS_PRICE
    if qty > 90:
        final_price *= 0.85
elif flowers == "Tulips":
    final_price = qty * TULIPS_PRICE
    if qty > 80:
        final_price *= 0.85
elif flowers == "Narcissus":
    final_price = qty * NARCISSUS_PRICE
    if qty < 120:
        final_price *= 1.15
elif flowers == "Gladiolus":
    final_price = qty * GLADIOULLS_PRICE
    if qty < 80:
        final_price *= 1.20

if final_price <= budget :
    print(f"Hey, you have a great garden with {qty} {flowers} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")


