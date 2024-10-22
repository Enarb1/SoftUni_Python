from collections import deque

SIZE = 8

def check_rank(player, player_pos):

    if player == "w":
        return player_pos[0] == 0
    return player_pos[0] == SIZE - 1


def check_diagonal(player_pos, board):

    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for diagonal in diagonals:
        pos = [player_pos[0] + diagonal[0], player_pos[1] + diagonal[1]]
        try:
            if board[pos[0]][pos[1]] != "-":
                return True
        except IndexError:
            pass
    return False


def get_matrix():
    matrix = []
    w = []
    b = []

    for row in range(SIZE):
        line = input().split()
        if "w" in line:
            w = [row, line.index("w")]
        if "b" in line:
            b = [row, line.index("b")]
        matrix.append(line)

    return matrix, w, b

def pawn_wars():
    board, w_pos, b_pos = get_matrix()

    rows = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1", 8: "0"}
    columns ={0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

    names = {
        "w": "White",
        "b": "Black"
    }

    positions  = {
        "w": w_pos,
        "b": b_pos
    }
    movement = {
        "w": (-1, 0),
        "b": (1, 0),
    }

    turns = deque(["w", "b"])

    while True:
        player = turns[0]
        player_pos = positions[player]

        if check_diagonal(player_pos, board):
            opponent = turns[-1]
            opponent_pos = positions[opponent]
            print(f"Game over! {names[player]} win, capture on {columns[opponent_pos[1]]}{rows[opponent_pos[0]]}.")
            break

        board[player_pos[0]][player_pos[1]] = "-"
        player_pos = [player_pos[0] + movement[player][0], player_pos[1] + movement[player][1]]
        positions[player] = player_pos
        board[player_pos[0]][player_pos[1]] = player

        if check_rank(player, player_pos):
            print(f"Game over! {names[player]} pawn is promoted to a queen "
                  f"at {columns[player_pos[1]]}{rows[player_pos[0]]}.")
            break

        turns.rotate()

pawn_wars()