input_string = input()
my_dict = {}

for char in input_string:
    if char != " ":
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1

for character, count in my_dict.items():
    print(f"{character} -> {count}")