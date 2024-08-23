def move(message, num_of_l):
    left_part = message[:num_of_l]
    right_part = message[num_of_l:]
    new_message = right_part + left_part
    message = new_message
    return message


def insert(message, index, value):
    new_message = message[:index] + value + message[index:]
    message = new_message
    return message


def change_all(message, value_to_replace, replacement):
    new_message = message.replace(value_to_replace, replacement)
    message = new_message
    return message


decoded_message = input()
while True:
    command = input()
    if command == 'Decode':
        break

    line_command = command.split('|')
    action = line_command[0]
    if action == 'Move':
        num_of_letters = int(line_command[1])
        decoded_message = move(decoded_message, num_of_letters)
    elif action == 'Insert':
        index = int(line_command[1])
        value = line_command[2]
        if 0 <= index <= len(decoded_message):
            decoded_message = insert(decoded_message, index, value)
    elif action == 'ChangeAll':
        substring = line_command[1]
        replacement_value = line_command[2]
        decoded_message = change_all(decoded_message, substring, replacement_value)

print("The decrypted message is:", decoded_message)
