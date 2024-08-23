def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
#def sum_numbers(a, b):
    #result = a + b
    #return result


#def subtract(c):
    #result = sum_numbers(num1, num2) - c
    #return result


#num1 = int(input())
#num2 = int(input())
#num3 = int(input())

#print(subtract(num3))
