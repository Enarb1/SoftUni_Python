SIZE = int(input())

SMALL_WIN = 100
PENALTY = 200
JACKPOT = 100000


def dash():
    game_board[player_pos[0]][player_pos[1]] = "-"


def check_position(row, col):
    return 0 <= row < SIZE and 0 <= col < SIZE


def game_over_print():
    print("Game over! You lost everything!")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

money = 100
player_pos = []
game_board = []

for row in range(SIZE):
    line = list(input())
    game_board.append(line)
    if "G" in line:
        player_pos = [row, line.index("G")]
        game_board[player_pos[0]][player_pos[1]] = "-"


while True:
    command = input()

    if command == "end":
        break

    direction = command
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    if not check_position(r, c):
        money = 0
        game_over_print()
        break

    player_pos = [r, c]
    if game_board[player_pos[0]][player_pos[1]] == "W":
        money += SMALL_WIN
        dash()
    elif game_board[player_pos[0]][player_pos[1]] == "J":
        money += JACKPOT
        dash()
        print("You win the Jackpot!")
        break
    elif game_board[player_pos[0]][player_pos[1]] == "P":
        money -= PENALTY
        dash()

    if money <= 0:
        game_over_print()
        break

game_board[player_pos[0]][player_pos[1]] = "G"

if money > 0:
    print(f"End of the game. Total amount: {money}$")
    print(*[''.join(row) for row in game_board], sep="\n")
