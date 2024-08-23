numbers_count = int(input())

odd_sum = 0
odd_max = float("-inf")
odd_min = float("inf")
even_sum = 0
even_max = float("-inf")
even_min = float("inf")

for index in range(1, numbers_count + 1):
    number = float(input())
    if index % 2 != 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
print(f"OddSum={odd_sum:.2f},")
if odd_min == float("inf"):
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == float("-inf"):
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == float("inf"):
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == float("-inf"):
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")