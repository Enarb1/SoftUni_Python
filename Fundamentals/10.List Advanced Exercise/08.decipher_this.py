def decipher(cod_lst):
    decoded = []

    for word in cod_lst:
        digits = "".join([num for num in word if num.isdigit()])
        letters = [l for l in word if l.isalpha()]
        letters[0], letters[-1] = letters[-1], letters[0]
        letters = ''.join(letters)
        digit_to_letter = chr(int(digits))
        deciphered_word = digit_to_letter + letters
        decoded.append(deciphered_word)

    return " ".join(decoded)


to_decipher = input().split()
print(decipher(to_decipher))