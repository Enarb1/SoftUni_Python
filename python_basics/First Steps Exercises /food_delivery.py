CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGI_MENU_PRICE = 8.15
DELIVERY = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegi_menu = int(input())

total_menus = (chicken_menu * CHICKEN_MENU_PRICE) + (fish_menu * FISH_MENU_PRICE) + (vegi_menu * VEGI_MENU_PRICE)
desert = 0.20 * total_menus
total_sum = total_menus + desert + DELIVERY

print(total_sum)

