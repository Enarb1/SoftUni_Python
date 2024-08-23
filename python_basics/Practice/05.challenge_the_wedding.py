male = int(input())
female = int(input())
tables = int(input())

places_total = tables * 2
contenders = male + female

while places_total > 0 or contenders > 0:
    for m in range(1, male + 1):
        for f in range(1, female + 1):
            print(f"({m} <-> {f})", end=" ")
            places_total -= 2
            if places_total <= 0 or contenders <= 0:
                exit()
        contenders -= 2
    if places_total <= 0 or contenders <= 0:
        break

