def contest_points(contestants_and_points, username, contest, points):

    if contest not in contestants_and_points.keys():
        contestants_and_points[contest] = {}
    if (username not in contestants_and_points[contest].keys()
            or contestants_and_points[contest][username] < points):
        contestants_and_points[contest][username] = points


def participants(contestants_and_points,users_score ):
    for contest, users in contestants_and_points.items():
        for name, score in users.items():
            if name not in users_score.keys():
                users_score[name] = 0
            users_score[name] += score


contestants_and_points = {}
users_score = {}
while True:
    command =input()
    if command == 'no more time':
        break

    info = command.split(" -> ")
    username = info[0]
    contest = info[1]
    points = int(info[2])

    contest_points(contestants_and_points, username, contest, points)

participants(contestants_and_points, users_score)

for contest, users in contestants_and_points.items():
    print(f'{contest}: {len(contestants_and_points[contest])} participants')
    sorted_score = sorted(contestants_and_points[contest].items(), key=lambda item: (-item[1], item[0]))
    n = 1
    for user, score in sorted_score:
        print(f'{n}. {user} <::> {score}')
        n += 1

sorted_standings = sorted(users_score.items(), key=lambda item: (-item[1], item[0]))
print('Individual standings:')
num = 1
for user, score in sorted_standings:
    print(f'{num}. {user} -> {score}')
    num += 1
