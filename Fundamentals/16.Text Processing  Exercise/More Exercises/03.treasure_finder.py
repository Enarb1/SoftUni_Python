keys = input().split()

while True:
    command = input()
    if command == 'find':
        break
    message = ''
    corresponding_keys = []
    length_keys = len(keys)
    for index, value in enumerate(command):
        corresponding_value = keys[index % length_keys]
        corresponding_keys.append(corresponding_value)
    for index, char in enumerate(command):
        letter = chr(ord(char) - int(corresponding_keys[index]))
        message += letter
    type_ = message[message.index('&') + 1:]
    final_type = type_[:type_.index('&')]
    coordinates = message[message.index('<') + 1:message.index('>')]
    print(f'Found {final_type} at {coordinates}')













