soldier_list = input().split(" ")
required_sequence = int(input())
soldiers = []
suicide_soldiers = []

for soldier in soldier_list:
    soldiers.append(int(soldier))

sequence = 0
index = 0
while soldiers:
    sequence += 1
    if sequence % required_sequence == 0:
        suicide_soldiers.append(soldiers[index])
        soldiers.pop(index)
        sequence = 0
    else:
        index += 1
    if index >= len(soldiers):
        index = 0

output = "[" + ",".join(map(str, suicide_soldiers)) + "]"
print(output)



