first_list = input().split()


while True:
    command = input().split()
    if 'end' in command:
        break
    elif 'exchange' in command:
        index = int(command[1])
        if index > len(first_list) or index < 0:
            print("Invalid index")
        else:
            left = first_list[index + 1:]
            right = first_list[:index + 1]
            first_list = []
            first_list.extend(left)
            first_list.extend(right)
    elif command[0] == 'max' or command[0] == 'min':
        max_even_index = "No matches"
        min_even_index = "No matches"
        max_odd_index = "No matches"
        min_odd_index = "No matches"
        even_max = float('-inf')
        odd_max = float('-inf')
        even_min = float('inf')
        odd_min = float('inf')
        for index, num in enumerate(first_list):
            if 'max' in command:
                if int(num) % 2 == 0:
                    if int(num) >= even_max:
                        even_max = int(num)
                        max_even_index = index
                elif int(num) % 2 != 0:
                    if int(num) >= odd_max:
                        odd_max = int(num)
                        max_odd_index = index
            elif 'min' in command:
                if int(num) % 2 == 0:
                    if int(num) < even_min:
                        even_min = int(num)
                        min_even_index = index
                elif int(num) % 2 != 0:
                    if int(num) < odd_min:
                        odd_min = int(num)
                        min_odd_index = index
        if 'max' in command and 'even' in command:
            print(max_even_index)
        elif "max" in command and "odd" in command:
            print(max_odd_index)
        elif 'min' in command and "even" in command:
            print(min_even_index)
        elif 'min' in command and 'odd' in command:
            print(min_odd_index)
    elif 'first' in command or 'last' in command:
        if int(command[1]) > len(first_list):
            print("Invalid count")
        elif 'first' in command:
            num_list = []
            for num in first_list:
                if 'even' in command:
                    if int(num) % 2 == 0:
                        num_list.append(num)
                        if len(num_list) == int(command[1]):
                            break
                elif 'odd' in command:
                    if int(num) % 2 != 0:
                        num_list.append(num)
                        if len(num_list) == int(command[1]):
                            break
            print(list(map(int, num_list)))
            num_list = []
        elif 'last' in command:
            last_num = []
            for num in first_list:
                if 'even' in command:
                    if int(num) % 2 == 0:
                        last_num.append(num)
                        if len(last_num) > int(command[1]):
                            last_num.pop(0)
                elif 'odd' in command:
                    if int(num) % 2 != 0:
                        last_num.append(num)
                        if len(last_num) > int(command[1]):
                            last_num.pop(0)
            print(list(map(int, last_num)))
            last_num = []
print(list(map(int,  first_list)))

