class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()

    if command == "End":
        break
    party.people.append(command)
total_people = ", ".join(party.people)
print(f"Going: {total_people}")
print(f"Total: {len(party.people)}")


