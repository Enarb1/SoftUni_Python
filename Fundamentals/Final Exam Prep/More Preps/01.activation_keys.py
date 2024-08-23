def slice_func(key, start_index, end_index):
    return key[:start_index] + key[end_index:]


def flip_func(key, flip_type, start_index, end_index):

    if flip_type == 'Upper':
        return key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
    elif flip_type == 'Lower':
        return key[:start_index] + key[start_index:end_index].lower() + key[end_index:]


def contains_func(key, substring):

    if substring in key:
        return f'{key} contains {substring}'
    else:
        return f'Substring not found!'


def process_commands(key):

    while True:
        command = input()
        if command == 'Generate':
            break
        actions = command.split('>>>')
        if actions[0] == 'Contains':
            substring = actions[1]
            print(contains_func(key, substring))
        elif actions[0] == 'Flip':
            flip_type = actions[1]
            start_index = int(actions[2])
            end_index = int(actions[3])
            new_key = flip_func(key, flip_type, start_index, end_index)
            key = new_key
            print(key)
        elif actions[0] == 'Slice':
            start_index = int(actions[1])
            end_index = int(actions[2])
            new_key = slice_func(key, start_index, end_index)
            key = new_key
            print(key)

    print(f'Your activation key is: {key}')


initial_key = input()
process_commands(initial_key)