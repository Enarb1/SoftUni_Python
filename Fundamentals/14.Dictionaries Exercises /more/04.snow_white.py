def add_dwarf(dwarfs_dict, name, hat_color, physics):
    if hat_color not in dwarfs_dict.keys():
        dwarfs_dict[hat_color] = {}
    if name not in dwarfs_dict[hat_color].keys() or dwarfs_dict[hat_color][name] < physics:
        dwarfs_dict[hat_color][name] = physics


def print_result():
    sorted_dwarfs = sorted(dwarfs.items(), key=lambda item: (-list(item[1].values())[0], (-len(item[1]))))
    for color, details in sorted_dwarfs:
        for name, physics in details.items():
            print(f'({color}) {name} <-> {physics}')


dwarfs = {}
hat_color_count = {}

while True:
    command = input()
    if command == 'Once upon a time':
        print_result()
        break
    info = command.split(" <:> ")
    dwarf_name = info[0]
    dwarf_hat_color = info[1]
    dwarf_physics = int(info[2])
    add_dwarf(dwarfs, dwarf_name, dwarf_hat_color, dwarf_physics)
