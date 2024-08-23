def change(friends_lst, index, new_name):
    if 0 <= index < len(friends_lst):
        current_name = friends_lst[index]
        friends_lst.pop(index)
        friends_lst.insert(index, new_name)
        print(f"{current_name} changed his username to {new_name}.")
        return True
    return False


def error(friends_lst, blacklist_lst, lost_lst, index):
    if 0 <= index < len(friends_lst):
        name = friends_lst[index]
        if name != "Blacklisted" and name != "Lost":
            lost_lst.append(name)
            print(f"{name} was lost due to an error.")
            for idx, lost_name in enumerate(friends_lst):
                if lost_name == name:
                    index = idx
                    friends_lst.pop(idx)
                    friends_lst.insert(index, "Lost")
            return True
    return False


def black_list(friends_lst, blacklist_lst, name):
    if name in friends_lst:
        blacklist_lst.append(name)
        print(f"{name} was blacklisted.")
        for idx, blacklisted_name in enumerate(friends_lst):
            if blacklisted_name == name:
                index = idx
                friends_lst.pop(index)
                friends_lst.insert(index, "Blacklisted")
    else:
        print(f"{name} was not found.")


def process_commands(friends_lst, commands, blacklist_lst, lost_lst):
    for command in commands:
        command_parts = command.split()
        if command_parts[0] == "Blacklist":
            name = command_parts[1]
            black_list(friends_lst, blacklist_lst, name)
        elif command_parts[0] == "Error":
            index = int(command_parts[1])
            error(friends_lst,blacklist_lst,lost_lst,index)
        elif command_parts[0] == "Change":
            index = int(command_parts[1])
            new_name = command_parts[2]
            change(friends_lst, index, new_name)
    return friends_lst, blacklist_lst, lost_lst


friends_list = input().split(", ")
commands_list = []
blacklist = []
lost_list = []

while True:
    cmnd = input()
    if cmnd == "Report":
        break
    commands_list.append(cmnd)
process_commands(friends_list, commands_list, blacklist, lost_list)
print(f"Blacklisted names: {len(blacklist)}")
print(f"Lost names: {len(lost_list)}")
print(" ".join(friends_list))
