todos = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    action = command.split('-')
    priority = int(action[0]) - 1
    task = action[1]
    todos.pop(priority)
    todos.insert(priority, task)

    result = [element for element in todos if element != 0]

print(result)




