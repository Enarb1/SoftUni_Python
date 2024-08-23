from math import floor
batch = int(input())
cup = 140
small_spoon = 10
big_spoon = 20
single_cookie_grams = 25
cookies_per_box = 5
total_boxes = 0
for _ in range(batch):
    flour = int(input())
    sugar = int(input())
    cocoa = int(input())
    flour_cups = flour / cup
    sugar_spoons = sugar / big_spoon
    cocoa_spoons = cocoa / small_spoon
    cookies_per_bake = (cup + small_spoon + big_spoon) * (min(flour_cups, sugar_spoons, cocoa_spoons) / single_cookie_grams)
    boxes = floor(cookies_per_bake / cookies_per_box)

    if boxes <= 0:
        print(f'Ingredients are not enough for a box of cookies.')
    else:
        total_boxes += boxes
        print(f'Boxes of cookies: {boxes}')
print(f'Total boxes: {total_boxes}')

