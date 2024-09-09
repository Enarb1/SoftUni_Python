ROWS = 6
COLS = 7

direction_mapper = {
    "up": (-1, 0),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
}


class FullColumnError(Exception):
    pass


def is_valid_place(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def check_directions(board, row_index, col_index, row_movement_index, col_movement_index, player_number, sign):
    count = 0
    for i in range(1, 4):
        current_row_index = eval(f"{row_index} {sign} {row_movement_index * i}")
        current_col_index = eval(f"{col_index} {sign} {col_movement_index * i}")

        if not is_valid_place(current_row_index, current_col_index):
            break

        if board[current_row_index][current_col_index] != player_number:
            break

        count += 1
    return count


def is_winner(board, row_index, col_index, player_number):

    for direction, values in direction_mapper.items():
        result = 1
        row_movement_index, col_movement_index = values
        direction_count = check_directions(board, row_index, col_index, row_movement_index, col_movement_index,
                                           player_number, "+")
        opposite_count = check_directions(board, row_index, col_index, row_movement_index, col_movement_index,
                                           player_number, "-")

        result += (direction_count + opposite_count)

        if result >= 4:
            return True
    return False


def player_choice(board,col_index, player_number):
    for row_index in range(len(game_board)-1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_number
            return row_index, col_index
    raise FullColumnError


def valid_choice(col_number):
    return 0 <= col_number <= COLS


def print_board(board):
    for data_row in board:
        print(data_row)


game_board = []

for _ in range(ROWS):
    game_board.append([0 for el in range(COLS)])

print_board(game_board)

turn = 1

while True:
    player_num = 1 if turn % 2 != 0 else 2

    try:
        selected_column = int(input(f"Player {player_num}, please choose a column: "))
    except ValueError:
        print("Please, enter a valid digit")
        continue

    if not valid_choice(selected_column):
        print(f"Please select a number between 1 and {COLS}")
        continue

    selected_col_index = selected_column - 1

    try:
        current_row, current_col = player_choice(game_board, selected_col_index, player_num)
    except FullColumnError:
        print("This column is full, please select another one")
        continue

    if is_winner(game_board, current_row, current_col, player_num):
        print(f"Winner!!! Player {player_num} you won!")
        break

    print_board(game_board)
    turn += 1

print_board(game_board)

