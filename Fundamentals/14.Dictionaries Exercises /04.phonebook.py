phonebook = {}

while True:
    command = input()
    if command.isdigit():
        break
    contact = command.split("-")
    name = contact[0]
    phone_number = contact[1]
    if name not in phonebook.items():
        phonebook[name] = phone_number
    phonebook[name] = phone_number

search_range = int(command)

for con_name in range(search_range):
    contact_name = input()
    if contact_name in phonebook.keys():
        print(f"{contact_name} -> {phonebook[contact_name]}")
    else:
        print(f"Contact {contact_name} does not exist.")

