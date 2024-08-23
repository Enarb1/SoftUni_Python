lenght = int(input())
width = int(input())
heigth = int(input())
accessoaries_percent = float(input()) / 100

total_volume_liters = (lenght * width * heigth) /1000
volume_needed = total_volume_liters * (1 - accessoaries_percent)

print(volume_needed)
