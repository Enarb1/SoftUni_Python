number = int(input())
bonus = 0  #създаваме си променлива

if number <= 100 :
    bonus = 5
elif number > 1000 : #тук слагаме пърео 1000  , защото иначе , ако числото е над 100 и над хиляда , няма да може да влезе за if-a над 100
    bonus = number * 0.1
else:
    bonus = number * 0.2

if number % 2 == 0: #дали е четно
    bonus = bonus + 1
elif number % 10 == 5: #дали е нечетно
    bonus = bonus + 2

print(bonus)
print(bonus + number)