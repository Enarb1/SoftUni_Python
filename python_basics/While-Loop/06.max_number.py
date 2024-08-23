MAX_NUMBER = float("-inf")

while True:
    text = input()

    if text == 'Stop':
        break

    current_number = int(text)

    if current_number > MAX_NUMBER:

        MAX_NUMBER = current_number
    else:
        continue
print(f"{MAX_NUMBER}")





