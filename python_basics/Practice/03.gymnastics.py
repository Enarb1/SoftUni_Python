MAX_POINTS = 20

country = input()
tool = input()

total_point = 0
level = 0
quality = 0

if country == "Russia":
    if tool == "ribbon":
        level += 9.100
        quality += 9.400
    elif tool == "hoop":
        level += 9.300
        quality += 9.800
    elif tool == "rope":
        level += 9.600
        quality += 9.000

elif country == "Bulgaria":
    if tool == "ribbon":
        level += 9.600
        quality += 9.400
    elif tool == "hoop":
        level += 9.550
        quality += 9.750
    elif tool == "rope":
        level += 9.500
        quality += 9.400
elif country == "Italy":
    if tool == "ribbon":
        level += 9.200
        quality += 9.500
    elif tool == "hoop":
        level += 9.450
        quality += 9.350
    elif tool == "rope":
        level += 9.700
        quality += 9.150

total_points = level + quality
diff = ((MAX_POINTS - total_points) / 20) * 100
print(f"The team of {country} get {total_points:.3f} on {tool}.")
print(f"{diff:.2f}%")