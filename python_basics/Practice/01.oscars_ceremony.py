rent = int(input())

statues_price = rent * 0.7
catering_price = statues_price * 0.85
sound_price = catering_price * 0.5

total_sum = rent + statues_price + catering_price + sound_price

print(f"{total_sum:.2f}")