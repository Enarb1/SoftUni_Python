def initial_dict(pieces, loop_range):

    for _ in range(loop_range):
        piece, composer, key = input().split('|')
        pieces[piece] = {}
        pieces[piece][composer] = key

    return pieces


def remove_piece(pieces, piece):
    if piece in pieces.keys():
        print(f'Successfully removed {piece}!')
        del pieces[piece]
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return pieces


def change_key(pieces, piece, new_key):

    if piece in pieces:
        for key, value in pieces[piece].items():
            pieces[piece][key] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')

    return pieces


def add_process(pieces, piece, composer, key):

    if piece not in pieces.keys():
        pieces[piece] = {}
        pieces[piece][composer] = key
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f'{piece} is already in the collection!')

    return pieces


def process_commands(pieces):

    while True:
        command = input()
        if command == 'Stop':
            break

        action = command.split('|')
        piece = action[1]

        if action[0] == 'Add':
            composer, key = action[2], action[3]
            add_process(pieces, piece, composer, key)

        elif action[0] == 'Remove':
            remove_piece(pieces, piece)

        elif action[0] == 'ChangeKey':
            new_key = action[2]
            change_key(pieces, piece, new_key)

    for piece in pieces:
        for composer, key in pieces[piece].items():
            print(f'{piece} -> Composer: {composer}, Key: {key}')


n = int(input())
pieces = {}
initial_dict(pieces, n)
process_commands(pieces)

