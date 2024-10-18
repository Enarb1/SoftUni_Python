from collections import deque

bowls_of_ramen  = [int(b) for b in input().split(", ")]
customers = deque([int(c) for c in input().split(", ")])

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)
    elif bowl < customer:
        customer -= bowl
        customers.appendleft(customer)


if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")