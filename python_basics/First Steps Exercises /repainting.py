NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BAGS_PRICE = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
hours_work = int(input())


sum_materials = (((nylon)+2)*NYLON_PRICE) + ((paint * 1.1) * PAINT_PRICE) + (thinner * THINNER_PRICE) + BAGS_PRICE
sum_work = (sum_materials * 0.30 ) * hours_work
total_sum = sum_materials + sum_work

print(total_sum)