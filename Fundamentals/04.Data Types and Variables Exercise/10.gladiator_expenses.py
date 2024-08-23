lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights // 2
swords_broken = lost_fights // 3
shields_broken = lost_fights // (3 * 2)
armor_repairs = shields_broken // 2

expense = (broken_helmets * helmet_price) + \
          (swords_broken * sword_price) + \
          (shields_broken * shield_price) + \
          (armor_repairs * armor_price)

print(f"Gladiator expenses: {expense:.2f} aureus")
