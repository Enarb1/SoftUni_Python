input_one = input().split(" ")
input_two = input().split(" ")
input_three = input().split(" ")

line_one = []
line_two = []
line_three = []
we_have_a_winner = False
winner = ""


for number in input_one:
    line_one.append(number)

for number in input_two:
    line_two.append(number)

for number in input_three:
    line_three.append(number)

for index_one, player_one in enumerate(line_one):
    for index_two, player_two in enumerate(line_two):
        for index_three, player_three in enumerate(line_three):
            if (index_one == index_two) and (index_one == index_three):
                if (player_one == player_two) and (player_one == player_three):
                    if player_one == "1" or player_one == "2":
                        we_have_a_winner = True
                        winner = player_one
                        break
            elif line_one[0] == line_two[1] and line_two[1] == line_three[2]:
                if line_one[0] == "1" or line_one[0] == "2":
                    we_have_a_winner = True
                    winner = line_one[0]
                    break
            elif line_one[2] == line_two[1] and line_two[1] == line_three[0]:
                if line_one[2] == "1" or line_one[2] == "2":
                    we_have_a_winner = True
                    winner = line_one[2]
                    break
if line_one[0] == line_one[1] and line_one[1] == line_one[2]:
    if line_one[0] == "1" or line_one[0] == "2":
        we_have_a_winner = True
        winner = line_one[0]
elif line_two[0] == line_two[1] and line_two[1] == line_two[2]:
    if line_two[0] == "1" or line_two[0] == "2":
        we_have_a_winner = True
        winner = line_two[0]
elif line_three[0] == line_three[1] and line_three[1] == line_three[2]:
    if line_three[0] == "1" or line_three[0] == "2":
        we_have_a_winner = True
        winner = line_three[0]

if we_have_a_winner:
    if winner == "1":
        print("First player won")
    elif winner == "2":
        print("Second player won")
else:
    print("Draw!")
