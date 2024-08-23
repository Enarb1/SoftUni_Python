from collections import deque

total_food = int(input())
customers = deque(map(int, input().split()))

print(max(customers))


# for _ in range(len(customers)):
#     if total_food >= customers[0]:
#         total_food -= customers.popleft()
#     else:
#         #orders_left = " ".join(map(str, customers))
#         print('Orders left:', *customers, sep=' ')
#         break
# if len(customers) == 0:
#     print('Orders complete')

while customers and total_food >= customers[0]:
    customer_demand = customers.popleft()
    total_food -= customer_demand

if len(customers) > 0:
    orders_left = " ".join(map(str, customers))
    print('Orders left:', *customers, sep=' ')
else:
    print('Orders complete')




