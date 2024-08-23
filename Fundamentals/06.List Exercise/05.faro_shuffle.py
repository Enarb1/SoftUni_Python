cards_string = input()
shuffles = int(input())
cards_list = cards_string.split(" ")

for _ in range(shuffles):
    half = len(cards_list) // 2
    left = cards_list[:half]
    right = cards_list[half:]

    shuffled_deck = []
    for index in range(half):
        shuffled_deck.append(left[index])
        shuffled_deck.append(right[index])

    cards_list = shuffled_deck

print(cards_list)