def groups(number_list):
    max_value = 10
    while number_list:
        filtered_lst = [num for num in number_list if num <= max_value]
        number_list = [num for num in number_list if num > max_value]
        print(f"Group of {max_value}'s: {filtered_lst}")
        max_value += 10

    return


input_lst = list(map(int,input().split(", ")))
groups(input_lst)