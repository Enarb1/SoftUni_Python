def output(nice_list, naughty_list, not_found_list):
    result = []
    if nice_list:
        result.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        result.append(f"Naughty: {', '.join(naughty_list)}")
    if not_found_list:
        result.append(f"Not found: {', '.join(not_found_list)}")

    return "\n".join(result)


def naughty_or_nice_list(kids_list, *commands, **keywords):
    nice_list = []
    naughty_list = []

    for command in commands:
        number, behavior = command.split('-')
        number = int(number)

        matching_kids = [kid for kid in kids_list if kid[0] == number]

        if len(matching_kids) == 1:
            kid = matching_kids[0]
            if behavior == "Nice":
                nice_list.append(kid[1])
            elif behavior == "Naughty":
                naughty_list.append(kid[1])
            kids_list.remove(kid)

    for name, behavior in keywords.items():
        matching_kids = [kid for kid in kids_list if kid[1] == name]

        if len(matching_kids) == 1:
            kid = matching_kids[0]
            if behavior == "Nice":
                nice_list.append(kid[1])
            elif behavior == "Naughty":
                naughty_list.append(kid[1])
            kids_list.remove(kid)

    not_found_list = [kid[1] for kid in kids_list]
    result = output(nice_list, naughty_list, not_found_list)
    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))