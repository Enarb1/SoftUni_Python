number_list = list(map(int,input().split(", ")))

found_index = map(lambda index: index if number_list[index] % 2 == 0 else "no", range(len(number_list)))

even_indexes = list(filter(lambda element: element != 'no', found_index))

print(even_indexes)