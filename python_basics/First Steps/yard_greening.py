PRICE_PER_SQM = 7.61
DISCOUNT = 0.18

square_meters_greening = float(input())

sum = square_meters_greening * PRICE_PER_SQM
discount_sum = sum * DISCOUNT
final_price = sum - discount_sum

print(f'The final prie is: {final_price} lv.')
print(f'The discount is: {discount_sum} lv.')
