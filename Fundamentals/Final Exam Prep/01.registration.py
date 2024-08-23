def letters(name, action_type):
    username = ''
    if action_type == 'Lower':
        return name.lower()
    elif action_type == 'Upper':
        return name.upper()


def reverse_user(name, start_i, end_i):
    username = name[start_i: end_i + 1]
    return username[::-1]


def substring(name, sub):

    if sub in name:
        return name.replace(sub, "")
    else:
        return f"The username {name} doesn't contain {sub}."


def replace_char(name, char):
    return name.replace(char, '-')


def is_valid(name, char):
    if char in name:
        return f"Valid username."
    else:
        return f"{char} must be contained in your username."


user = input()

while True:
    command = input()
    if command == 'Registration':
        break

    action = command.split()
    if action[0] == "Letters":
        replace_type = action[1]
        user = letters(user, replace_type)
        print(user)
    elif action[0] == 'Reverse':
        start_index = int(action[1])
        end_index = int(action[2])
        if (start_index >= 0 and end_index >= 0 and end_index < len(user)):
            print(reverse_user(user, start_index, end_index))
    elif action[0] == 'Substring':
        substitute = action[1]
        user = substring(user, substitute)
        print(user)
    elif action[0] == 'Replace':
        character = action[1]
        user = replace_char(user, character)
        print(user)
    elif action[0] == 'IsValid':
        validation_char = action[1]
        print(is_valid(user, validation_char))