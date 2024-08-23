def substitute(text, substring, substitute_string):

    if substring in text:
        text = text.replace(substring, substitute_string)
        print(text)
    else:
        print('Nothing to replace!')

    return text


def cut(text, index, length):
    text = text[:index] + text[index + length:]
    print(text)
    return text


def take_odd(text):
    new_pass = ''
    for index, char in enumerate(text):
        if index % 2 != 0:
            new_pass += char
    text = new_pass
    print(text)
    return text


def process_commands(text):

    while True:
        command = input()
        if command == 'Done':
            break
        line_input = command.split()
        action = line_input[0]
        if action == 'TakeOdd':
            text = take_odd(text)
        elif action == 'Cut':
            index = int(line_input[1])
            length = int(line_input[2])
            text = cut(text, index, length)
        elif action == 'Substitute':
            substring = line_input[1]
            substitute_string = line_input[2]
            text = substitute(text, substring, substitute_string)
    print(f'Your password is: {text}')


text_input = input()
process_commands(text_input)
