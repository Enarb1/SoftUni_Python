def even_words(words_list):

    words = [word for word in words_list if len(word) % 2 == 0]

    return words


input_string = input().split()
[print(word)for word in even_words(input_string)]