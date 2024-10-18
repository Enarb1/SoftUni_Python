def words_sorting(*words):

    words_value = {}

    for word in words:
        words_value[word] = sum([ord(c) for c in word])

    total_sum = sum(words_value.values())
    is_even = (total_sum % 2 == 0)

    sorted_words = sorted(words_value.items(),key=lambda x: (x[0] if is_even else -x[1]))

    return '\n'.join(f"{key} - {value}" for key, value in sorted_words)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))