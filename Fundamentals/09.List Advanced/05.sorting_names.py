
def sorted_names(names_list):

    sorted_list = sorted(names_list, key=lambda name: (-len(name), name))
    return sorted_list


input_string = input().split(", ")
print(sorted_names(input_string))