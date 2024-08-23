budget = float(input())

flour_one_kg_price = float(input())
pack_of_eggs_price = flour_one_kg_price * 0.75
milk_price_liter = (flour_one_kg_price * 0.25) + flour_one_kg_price
milk_needed = 0.25 * milk_price_liter

loaves = 0
colored_eggs = 0
money_needed_for_a_loaf = flour_one_kg_price + pack_of_eggs_price + milk_needed

while budget >= money_needed_for_a_loaf:
    loaves += 1
    budget -= money_needed_for_a_loaf
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
    if budget >= money_needed_for_a_loaf:
        continue
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
