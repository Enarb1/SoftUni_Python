
def action(type_of_value, input_value):
    if type_of_value == "int":
        return int(input_value) * 2
    elif type_of_value == 'real':
        return f"{float(input_value) * 1.5:.2f}"
    elif type_of_value == "string":
        return f"${input_value}$"


type_of_input = input()
value = input()
print(action(type_of_input, value))
