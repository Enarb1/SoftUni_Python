months = int(input())

WATER_PER_MONTH = 20
INTERNET_PER_MONTH = 15
water_total = WATER_PER_MONTH * months
internet_total = INTERNET_PER_MONTH * months
el_bill_total = 0
other = 0

for _ in range(1, months + 1):
    el_bill = float(input())
    el_bill_total += el_bill
    other += el_bill + WATER_PER_MONTH + INTERNET_PER_MONTH + ((el_bill + WATER_PER_MONTH + INTERNET_PER_MONTH) * 0.2)
print(f"Electricity: {el_bill_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {(water_total + internet_total + el_bill_total + other) / months:.2f} lv")
