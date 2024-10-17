from collections import deque

def last_line_print(textiles, medicaments):
    line_print = ""

    if medicaments:
        line_print += f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}\n"

    if textiles:
        line_print += f"Textiles left: {', '.join(map(str, textiles))}"

    return line_print


def sorted_items_print(items):
    items_print = ""
    sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
    for k, v in sorted_items:
        items_print += f"{k} - {v}\n"

    return items_print


def first_line_print(textiles, medicaments, items):
    condition_mapper = {
        (False, False): "Textiles and medicaments are both empty.\n",
        (False, True): "Textiles are empty.\n",
        (True, False): "Medicaments are empty.\n"
    }

    textiles_cond = bool(textiles)
    medicaments_cond = bool(medicaments)

    return condition_mapper.get((textiles_cond, medicaments_cond))


def final_print(textiles, medicaments, items):
    message = first_line_print(textiles, medicaments, items)
    if items:
        message += sorted_items_print(items)

    message += last_line_print(textiles, medicaments)

    return message


def check_items(items, value):
    if value not in items.keys():
        items[value] = 0
    items[value] += 1

    return items


def apocalypse_preparation():
    textiles = deque([int(t) for t in input().split()])
    medicaments = [int(m) for m in input().split()]

    items = {}
    mapper = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
    }

    while textiles and medicaments:
        textile = textiles.popleft()
        medicament = medicaments.pop()
        value = textile + medicament

        if value in mapper.keys():
            items = check_items(items, mapper[value])
        elif value > 100:
            items = check_items(items, mapper[100])
            to_add = value - 100
            medicaments[-1] += to_add
        else:
            medicament += 10
            medicaments.append(medicament)

    return final_print(textiles, medicaments, items)

print(apocalypse_preparation())
