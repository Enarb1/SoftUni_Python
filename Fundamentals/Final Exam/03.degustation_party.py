def like(guests, guest, meal):
    if guest not in guests.keys():
        guests[guest] = []
    if meal not in guests[guest]:
        guests[guest].append(meal)
    return guests


def dislike(guests, guest, meal):
    if guest not in guests.keys():
        print(f'{guest} is not at the party.')
    elif meal not in guests[guest]:
        print(f"{guest} doesn't have the {meal} in his/her collection.")
    else:
        print(f"{guest} doesn't like the {meal}.")
        guests[guest].remove(meal)
        guests['Unlike'] += 1
    return guests


def degustation_party():
    guests = {'Unlike': 0}
    while True:
        command = input()
        if command == 'Stop':
            break
        action, guest, meal = command.split('-')
        if action == 'Like':
            guests = like(guests, guest, meal)
        if action == 'Dislike':
            guests = dislike(guests, guest, meal)

    for name in guests.keys():
        if not name == "Unlike":
            meals = ", ".join([meal for meal in guests[name]])
            print(f'{name}: {meals}')
    unlike_count = guests['Unlike']
    print(f'Unliked meals: {unlike_count}')

degustation_party()