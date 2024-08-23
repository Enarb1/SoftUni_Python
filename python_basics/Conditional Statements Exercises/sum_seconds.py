time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third  #тук създаваме# променлива, от която ще превърнем секундите в минути и секунди

minutes = total_time // 60 #по този начин вижаме колко пъти 60  може да се нанесе в тотал тайм
seconds = total_time % 60 #тук ни интересува колко е остаакът от тотал тайм като се нанесе 60

if seconds  < 10 :  #ако е под 10 секунди трябва да принтиира и една 0 преди резулатата
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
