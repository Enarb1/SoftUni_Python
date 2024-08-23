def activation_key(key):

    while True:
        command = input()
        if command == 'Generate':
            break

        line_input = command.split(">>>")
        action = line_input[0]

        if action == 'Contains':
            substring = line_input[1]
            if substring in key:
                print(f'{key} contains {substring}')
            else:
                print(f'Substring not found!')
        elif action == 'Flip':
            flip_type = line_input[1]
            start_index = int(line_input[2])
            end_index = int(line_input[3])
            new_key = ''
            if flip_type == 'Upper':
                new_key = key[:start_index] + (key[start_index:end_index]).upper() + key[end_index:]
            elif flip_type == 'Lower':
                new_key = key[:start_index] + (key[start_index:end_index]).lower() + key[end_index:]
            key = new_key
            print(key)
        elif action == 'Slice':
            start_index = int(line_input[1])
            end_index = int(line_input[2])
            new_key = key[:start_index] + key[end_index:]
            key = new_key
            print(key)
    print(f"Your activation key is: {key}")


initial_key = input()
activation_key(initial_key)
