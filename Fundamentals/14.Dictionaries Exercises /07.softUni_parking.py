def register(registered_users, user, license_plate):
    if user not in registered_users.keys():
        registered_users[user] = license_plate
        print(f"{user} registered {license_plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {license_plate}")

    return registered_users


def unregister(registered_users, user):
    if user in registered_users.keys():
        registered_users.pop(user)
        print(f"{user} unregistered successfully")
    else:
        print(f"ERROR: user {user} not found")
    return registered_users


loop_range = int(input())
registered_users = {}

for user in range(loop_range):
    data = input().split()
    action = data[0]
    username = data[1]
    if action == 'register':
        license_plate = data[2]
        register(registered_users,username, license_plate)
    elif action == 'unregister':
        unregister(registered_users,username)

for user, license_plate in registered_users.items():
    print(f"{user} => {license_plate}")

