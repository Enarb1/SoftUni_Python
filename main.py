def is_followed_by_zeroes(n):
    return str(n)[1:] == "0" * (len(str(n)) -1)


def all_digits_are_same(n):
    return len(set(str(n))) == 1


def is_incrementing(n):
    s = str(n)
    return all((int(s[i]) + 1) % 10 == int(s[i + 1]) for i in range(len(s) - 1))


def is_decrementing(n):
    s = str(n)
    return all((int(s[i]) - 1) % 10 == int(s[i + 1]) for i in range(len(s) - 1))


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def is_in_awsome_phrases(n, awsome_phrases):
    return n in awsome_phrases

    
def is_interesting_number(n, awesome_phrases):
    if n < 100:
        return False
    return (is_followed_by_zeroes(n) or
            all_digits_are_same(n) or
            is_incrementing(n) or
            is_decrementing(n) or
            is_palindrome(n) or
            is_in_awsome_phrases(n, awesome_phrases))


def is_interesting(number, awesome_phrases):
    if is_interesting_number(number, awesome_phrases):
        return 2
    if is_interesting_number(number + 1, awesome_phrases) or is_interesting_number(number + 2, awesome_phrases):
        return 1
    return 0


print(is_interesting(11209, [1337, 256]))
