last_sector = input()
rows_first_sector = int(input())
seats_odd_rows = int(input())

total_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 == 0:
            seats = seats_odd_rows + 2
        else:
            seats = seats_odd_rows
        for seat in range(1, seats + 1):
            print(chr(sector) + str(row) + chr(96 + seat))
            total_seats += 1
    rows_first_sector += 1
print(total_seats)