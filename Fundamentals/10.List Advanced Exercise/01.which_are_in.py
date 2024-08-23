def which_are_in(roots_list, in_words_to_look_lst):

    words = [word for word in roots_list if any(word in w for w in in_words_to_look_lst)]
    return words


root_words_lst = input().split(", ")
words_lst = input().split(", ")

print(which_are_in(root_words_lst, words_lst))