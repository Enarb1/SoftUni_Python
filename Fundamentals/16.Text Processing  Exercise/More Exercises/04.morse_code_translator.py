morse_message = input().split(' | ')
dictionary = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
              '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
              '---': 'o',
              '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w',
              '-..-': 'x',
              '-.--': 'y', '--..': 'z'}
message = ''
for word in morse_message:
    letters = word.split()
    w = ''
    for letter in letters:
        if letter in dictionary.keys():
            l = dictionary[letter].capitalize()
            w += l
    message += w + " "
print(message.strip())