from math import ceil

tv_show = input()
show_lenght = int(input())
break_lenght = int(input())

lunchtime = break_lenght * 1/8
naptime = break_lenght * 1/4

time_left = break_lenght - (lunchtime + naptime)
difference = abs(show_lenght - time_left)

if time_left >= show_lenght:
    print(f'You have enough time to watch {tv_show} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_show}, you need {ceil(difference)} more minutes.")