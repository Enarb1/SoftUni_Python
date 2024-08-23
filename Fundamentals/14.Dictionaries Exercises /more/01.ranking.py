def valid_contest_and_pass(contest_and_passwords,topic,password):

    for contest, passcode in contests_and_passwords.items():
        if contest == topic:
            if passcode == password:
                return True
    return False


def add_user(users_contests, contest, user, score ):

    if user not in users:
        users[user] = {contest: score}
    else:
        if contest in users[user].keys():
            if users[user][contest] < score:
                users[user][contest] = score
        else:
            users[user][contest] = score



contests_and_passwords = {}
users = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest_pass = command.split(":")
    contest = contest_pass[0]
    password = contest_pass[1]
    if contest not in contests_and_passwords.keys():
        contests_and_passwords[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    information = command.split("=>")
    topic = information[0]
    pass_code = information[1]
    username = information[2]
    points = int(information[3])

    if valid_contest_and_pass(contests_and_passwords, topic, pass_code):
        for cont, key, in contests_and_passwords.items():
            if cont == topic:
                if pass_code == key:
                    add_user(users, topic, username, points)

best_student = ''
max_score = 0

for student in users.keys():
    total_points = 0
    for topic, score in users[student].items():
        total_points += score
    if total_points > max_score:
        max_score = total_points
        best_student = student
print(f'Best candidate is {best_student} with total {max_score} points.')
print('Ranking:')
for user in sorted(users):
    print(user)
    sorted_score = sorted(users[user].items(), key=lambda item: item[1], reverse=True)
    for subject, score in sorted_score:
        print(f'#  {subject} -> {score}')



