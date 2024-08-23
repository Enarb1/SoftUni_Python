types_of_fire = input().split("#")
needed_water = int(input())
total_effort = 0
total_fire = 0

print("Cells:")
for fire in types_of_fire:
    current_fire = fire.split(" = ")
    fire_type = current_fire[0]
    cell = int(current_fire[1])
    if needed_water >= cell:
        cell_valid = False
        if fire_type == "High" and 80 < cell < 126:
            cell_valid = True
            needed_water -= cell
            total_effort += 0.25 * cell
            total_fire += cell
        elif fire_type == "Medium" and 50 < cell < 81:
            cell_valid = True
            needed_water -= cell
            total_effort += 0.25 * cell
            total_fire += cell
        elif fire_type == "Low" and 0 < cell < 51:
            cell_valid = True
            needed_water -= cell
            total_effort += 0.25 * cell
            total_fire += cell
        if cell_valid:
            print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")


