number = int(input())
number_string= str(number)
number_to_sort = ""

for digit in number_string:
    number_to_sort += digit

sorted_number = sorted(number_to_sort, reverse=True)

largest_number = int("".join(sorted_number))

print(largest_number)





