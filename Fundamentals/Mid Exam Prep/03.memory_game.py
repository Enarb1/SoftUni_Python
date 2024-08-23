def indexes_inpt(sequence_lst, indexes_input):
    if (int(indexes_input[0]) > len(sequence) - 1) or \
            (int(indexes_input[1]) > len(sequence) - 1) or \
            (int(indexes_input[0]) < 0) or \
            (int(indexes_input[1]) < 0) or \
            (indexes_input[0] == indexes_input[1]):
        invalid(sequence_lst, index_input)
    elif sequence[int(indexes_input[0])] == sequence[int(indexes_input[1])]:
        found_matching(sequence_lst,indexes_input)
    elif sequence[int(indexes_input[0])] != sequence[int(indexes_input[1])]:
        print("Try again!")


def invalid(sequence_lst, index_input):
    middle_i = len(sequence) // 2
    element_to_add = "-" + str(moves) + 'a'
    sequence.insert(middle_i, element_to_add)
    sequence.insert(middle_i + 1, element_to_add)
    print("Invalid input! Adding additional elements to the board")


def found_matching(sequence_lst, indexes_input ):
    element = sequence[int(indexes_input[0])]
    sequence.pop(int(indexes_input[0]))
    sequence.remove(element)
    print(f"Congrats! You have found matching elements - {element}!")


sequence = input().split()
moves = 0

while True:
    command = input()
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    if command == 'end':
        result = " ".join(sequence)
        print(f"Sorry you lose :(")
        print(f"{result}")
        break
    index_input = command.split()
    moves += 1
    indexes_inpt(sequence, index_input)

