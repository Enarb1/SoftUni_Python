from collections import deque

seats = input().split(", ")

first_seq = deque([int(x) for x in input().split(", ")])
second_seq = deque([int(y) for y in input().split(", ")])


matched_seats = []
rotations = 0
seats_taken = 0

while rotations < 10 and seats_taken < 3:
    num1 = first_seq.popleft()
    num2 = second_seq.pop()
    letter = chr(num1 + num2)
    rotations += 1
    seat1, seat2 = str(num1) + letter, str(num2) + letter

    if seat1 in seats or seat2 in seats:
        matched_seat = next((seat for seat in (seat1, seat2) if seat in seats), None)
        if matched_seat not in matched_seats:
            seats_taken += 1
            matched_seats.append(matched_seat)
        continue

    first_seq.append(num1)
    second_seq.appendleft(num2)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")






