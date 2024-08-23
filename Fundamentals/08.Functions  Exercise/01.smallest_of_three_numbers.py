
def smallest(some_list: list) -> int:
    return min(some_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest([first_number, second_number, third_number])
print(smallest_number)

#num1 = int(input())
#num2 = int(input())
#num3 = int(input())

#min_number = lambda a, b, c: min(a,b,c)

#result = min_number(num1, num2, num3)

#print(result)