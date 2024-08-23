n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if n2 == 0 and operator == "/":
    print(f"Cannot divide {n1} by zero")
    exit()
elif operator == "/":
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")
    exit()
elif n2 == 0 and operator == "%":
    print(f"Cannot divide {n1} by zero")
    exit()
elif operator == "%":
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")
    exit()
elif operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
if result % 2 == 0:
    print(f"{n1} {operator} {n2} = {result} - even ")
else:
    print(f"{n1} {operator} {n2} = {result} - odd ")



