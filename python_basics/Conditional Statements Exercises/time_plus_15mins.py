hour = int(input())
minutes = int(input())
minutes = minutes + 15

if minutes >= 60: #ако са над 60мин . се добавят часове и се вадят 60 минути
    hour += 1
    minutes -= 60
if hour > 23:
    hour = 0

if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')