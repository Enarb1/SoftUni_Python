budget = float(input())
videocard_qty = int(input())
processor_qty = int(input())
ram_qty = int(input())

videocard_price_per_item = 250
videcards_total_cost = videocard_price_per_item * videocard_qty
processor_price_per_item = videcards_total_cost * 0.35
processors_total_cost = processor_price_per_item * processor_qty
ram_price_per_item = videcards_total_cost * 0.10
rams_total_cost = ram_price_per_item * ram_qty

total_sum = videcards_total_cost + processors_total_cost + rams_total_cost

if videocard_qty > processor_qty :
    total_sum = total_sum - (total_sum * 0.15)

difference = abs(total_sum - budget)

if total_sum <= budget :
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')







