from collections import deque

chocolate_stack = [int(n) for n in input().split(', ')]
milk_que = deque(int(n) for n in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolate_stack and milk_que:
    choco = chocolate_stack.pop()
    milk = milk_que.popleft()

    if choco <= 0 and milk <= 0:
        continue
    elif choco <= 0:
        milk_que.appendleft(milk)
        continue
    elif milk <= 0:
        chocolate_stack.append(choco)
        continue
    if choco == milk:
        milkshakes += 1
    else:
        new_choco = choco - 5
        milk_que.append(milk)
        chocolate_stack.append(new_choco)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join(str(x) for x in chocolate_stack) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk_que) or 'empty'}")
