total_tickets = 0
student_tickets = 0
kids_tickets = 0
standard_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break
    else:
        movie_name = command
        capacity = int(input())
        full_places = 0
        while True:
            command2 = input()
            if command2 == "End":
                break
            elif command2 == "student":
                student_tickets += 1
            elif command2 == "standard":
                standard_tickets += 1
            elif command2 == "kid":
                kids_tickets += 1

            full_places += 1
            total_tickets += 1

            if capacity == full_places:
                break
        print(f"{movie_name} - {(full_places / capacity)*100:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets)*100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets)*100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets)*100:.2f}% kids tickets.")