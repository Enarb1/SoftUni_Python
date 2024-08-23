def insert_space(text, index):

    text = text[:index] + " " + text[index:]
    print(text)
    return text


def reverse_substring(text, substring):
    if substring in text:
        start_index = text.find(substring)
        end_index = start_index + len(substring)
        text = text[:start_index] + text[end_index:] + substring[::-1]
        print(text)
    else:
        print('error')
    return text


def change_all(text, substring, replacement):

    text = text.replace(substring, replacement)
    print(text)
    return text


def process_commands(text):

    while True:
        command = input()
        if command == 'Reveal':
            break
        line_input = command.split(":|:")
        action = line_input[0]
        if action == 'InsertSpace':
            index = int(line_input[1])
            text = insert_space(text, index)
        elif action == 'Reverse':
            substring = line_input[1]
            text = reverse_substring(text, substring)
        elif action == 'ChangeAll':
            substring = line_input[1]
            replacement_string = line_input[2]
            text = change_all(text, substring, replacement_string)
    print(f'You have a new text message: {text}')


initial_text = input()
process_commands(initial_text)