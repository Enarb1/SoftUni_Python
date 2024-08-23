number = int(input())

even_sum = 0
odd_sum = 0

for i in range(number):
    current_number = int(input())

    if i % 2 == 0:
        even_sum = current_number + even_sum
    else:
        odd_sum = current_number + odd_sum

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {even_sum} ")
else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {diff} ")