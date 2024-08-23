def is_valid(username):
    if not (2 < len(username) < 17):
        return False

    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False

    return True


usernames_lst = input().split(", ")

for user in usernames_lst:
    if is_valid(user):
        print(user)
