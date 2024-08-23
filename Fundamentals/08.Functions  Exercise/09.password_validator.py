
def password_validity(password):

    word_input = password
    errors = []
    digits = 0

    if not 5 < len(word_input) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not word_input.isalnum():
        errors.append("Password must consist only of letters and digits")

    for value in word_input:
        if value.isdigit():
            digits += 1
    if digits < 2:
        errors.append("Password must have at least 2 digits")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


input_string = input()
password_validity(input_string)










