string_input = input()
rage_quit_message = ''
current_symbols = ''
symbols_count = 0

for index, char in enumerate(string_input):
    if char.isdigit():
        num = ''
        num += char
        if string_input[index + 1].isdigit():
            num += string_input[index + 1]
        num = int(num)
        current_symbols = current_symbols.upper()
        rage_quit_message += current_symbols * num
        current_symbols = ''
    else:
        current_symbols += char
        if char.upper() not in rage_quit_message:
            symbols_count += 1

print(f'Unique symbols used: {symbols_count}')
print(f'{rage_quit_message}')