MIN_NUMBER = float("inf")

while True:
    text = input()

    if text == 'Stop':
        break

    current_number = int(text)

    if current_number < MIN_NUMBER:

        MIN_NUMBER = current_number
    else:
        continue
print(f"{MIN_NUMBER}")





