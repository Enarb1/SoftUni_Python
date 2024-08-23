seq_one = set(int(n) for n in input().split())
seq_two = set(int(n) for n in input().split())

functions = {
    'Add First': lambda x: [seq_one.add(int(el)) for el in x],
    'Add Second': lambda x: [seq_two.add(int(el)) for el in x],
    'Remove First': lambda x: [seq_one.discard(int(el)) for el in x],
    'Remove Second': lambda x: [seq_two.discard(int(el)) for el in x],
    'Check Subset': lambda x: print(seq_one.issubset(seq_two) or seq_two.issubset(seq_one)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + ' ' + second_command

    functions[command](data)

print(*sorted(seq_one), sep=', ')
print(*sorted(seq_two), sep=', ')
