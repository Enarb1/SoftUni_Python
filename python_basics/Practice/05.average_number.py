numbers_qty = int(input())
cycle = 0
total_sum = 0

while True:
    num = int(input())
    cycle += 1
    total_sum += num
    if cycle == numbers_qty:
        print(f"{total_sum / cycle:.2f}")