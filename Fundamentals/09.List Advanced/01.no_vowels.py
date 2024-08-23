
def remove_vowels(text):
    vowels = "aeiou"
    new_text = "".join([char for char in text if char.lower() not in vowels])

    return new_text


word = input()
new_word = remove_vowels(word)
print(new_word)