class FriendsList:

        def __init__(self, friends_list):
            self.friends_list = friends_list
            self.blacklist = []
            self.lost = []

        def index_validation(self, index):
            if 0 <= index < len(self.friends_list):
                return True
            return False

        def black_list(self, name):
            if name in self.friends_list:
                self.blacklist.append(name)
                print(f"{name} was blacklisted ")
                index = self.friends_list.index(name)
                self.friends_list[index] = "Blacklisted"
            else:
                print(f"{name} was not found.")

        def error(self, index):
            name = self.friends_list[index]
            if name != "Blacklisted" and name != "Lost":
                self.lost.append(name)
                print(f"{name} was lost due to an error.")
                self.friends_list[index] = "Lost"

        def change(self, index, new_name):
            current_name = self.friends_list[index]
            self.friends_list[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

        def process_commands(self,commands):
            for command in commands:
                command_parts = command.split()
                action = command_parts[0]
                if action == "Blacklist":
                    name = command_parts[1]
                    self.black_list(name)
                elif action == "Error":
                    index = int(command_parts[1])
                    if self.index_validation(index) :
                        self.error(index)
                elif action == "Change":
                    index = int(command_parts[1])
                    new_name = command_parts[2]
                    if self.index_validation(index):
                        self.change(index, new_name)

        def report(self):
            print(f"Blacklisted names: {len(self.blacklist)}")
            print(f"Lost names: {len(self.lost)}")
            print(" ".join(self.friends_list))


friends_lst = input().split(", ")
commands_list = []
while True:
    command = input()
    if command == "Report":
        break
    commands_list.append(command)

manager = FriendsList(friends_lst)
manager.process_commands(commands_list)
manager.report()



