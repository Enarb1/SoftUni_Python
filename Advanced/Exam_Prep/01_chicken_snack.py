from collections import deque


def print_result(food_count):
    if food_count == 0:
        return "Henry remained hungry. He will try next weekend again."
    elif food_count >= 4:
        return f"Gluttony of the day! Henry ate {food_count} foods."
    else:
        return f"Henry ate: {food_count} food{'s' if food_count != 1 else ''}."


money = [int(x) for x in input().split()]
foods = deque(map(int, input().split()))

food_ate_count = 0
while money and foods:

    cash = money.pop()
    food_price = foods.popleft()

    if cash > food_price:
        food_ate_count += 1
        spare_change = cash - food_price
        if money:
            money[-1] += spare_change
    elif cash == food_price:
        food_ate_count += 1
        spare_change = 0

print(print_result(food_ate_count))