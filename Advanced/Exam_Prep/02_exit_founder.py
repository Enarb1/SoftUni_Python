from collections import deque

SIZE = 6

def get_matrix():
    return [[el for el in input().split()]for _ in range(SIZE)]

def exit_finder():
    player1, player2 = input().split(", ")
    play_field = get_matrix()
    gameplay = deque([player1, player2])

    resting_players = []

    while True:
        player = gameplay[0]
        position = eval(input())
        gameplay.rotate()

        if player in resting_players:
            resting_players.remove(player)
            continue

        if play_field[position[0]][position[1]] == "E":
            print(f"{player} found the Exit and wins the game!")
            break

        if play_field[position[0]][position[1]] == "T":
            print(f"{player} is out of the game! The winner is {gameplay[0]}.")
            break

        if play_field[position[0]][position[1]] == "W":
            print(f"{player} hits a wall and needs to rest.")
            resting_players.append(player)

exit_finder()



