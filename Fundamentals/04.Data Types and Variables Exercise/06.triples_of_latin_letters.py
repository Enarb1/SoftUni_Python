letters_to_read = int(input())

for letter_one in range(97, 97 + letters_to_read):
    for letter_two in range(97, 97 + letters_to_read):
        for letter_three in range(97, 97 + letters_to_read):
            print(f"{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}")