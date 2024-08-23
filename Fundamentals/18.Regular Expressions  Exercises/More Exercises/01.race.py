import re

def get_player_info(text):

    pattern = r'([a-zA-Z]+)|([0-9])'
    matches = re.finditer(pattern, text)
    name = ''
    distance = 0
    for match in matches:
        if match.group(1):
            name += match.group(1)
        elif match.group(2):
            distance += int(match.group(2))

    return {name: distance}


def get_results(results_dict, player, distance):

    if player not in results_dict.keys():
        results_dict[player] = 0
    results_dict[player] += distance


participants = input().split(", ")
results = {}
while True:
    command = input()
    if command == 'end of race':
        break

    text_input = command
    current_participant = get_player_info(text_input)
    for name, distance in current_participant.items():
        if name in participants:
            get_results(results, name, distance)

sorted_results = sorted(results.items(), key=lambda item: -item[1])
sorted_results = sorted_results[:3]
print(f'1st place: {sorted_results[0][0]}\n'
      f'2nd place: {sorted_results[1][0]}\n'
      f'3rd place: {sorted_results[2][0]}')





