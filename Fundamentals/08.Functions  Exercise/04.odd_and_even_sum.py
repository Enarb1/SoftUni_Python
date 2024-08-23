def odd_sum(num):
    numb_list = list(str(num))
    odd_total = 0
    for odd_num in numb_list:
        if int(odd_num) % 2 != 0:
            odd_total += int(odd_num)

    return odd_total


def even_sum(num):
    number_list = list(str(num))
    even_total = 0
    for even_num in number_list:
        if int(even_num) % 2 == 0:
            even_total += int(even_num)
    return even_total


number_input = int(input())
print(f"Odd sum = {odd_sum(number_input)}, Even sum = {even_sum(number_input)}")


