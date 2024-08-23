
def numbers_types(numbers_list):

    positive_nums = map(str, [num for num in numbers_list if num >= 0])
    negative_nums = map(str, [num for num in numbers_list if num < 0])
    even_nums = map(str, [num for num in numbers_list if num % 2 == 0])
    odd_nums = map(str, [num for num in numbers_list if num % 2 != 0])

    return (f'Positive: {", ".join(positive_nums)}\n'
            f'Negative: {", ".join(negative_nums)}\n'
            f'Even: {", ".join(even_nums)}\n'
            f'Odd: {", ".join(odd_nums)}')


numbers_lst = list(map(int, input().split(", ")))
print(numbers_types(numbers_lst))