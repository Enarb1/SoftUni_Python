import os

while True:
    command, *file_info = input().split('-')

    if command == "End":
        break
    if command == "Create":
        with open(f"files/{file_info[0]}", "w"):
            pass
    elif command == "Add":
        with open(f"files/{file_info[0]}", "a") as file:
            file.write(f"{file_info[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{file_info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(file_info[1], file_info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"files/{file_info[0]}")
        except FileNotFoundError:
            print("An error occurred")


