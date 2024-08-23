male = int(input())
female = int(input())
tables = int(input())

places_total = tables * 2
males_total = male
females_total = female


while places_total > 0 and males_total > 0 and females_total > 0:
    for m in range(1, male + 1):
        for f in range(1, female + 1):
            print(f"({m} <-> {f})", end=" ")
            places_total -= 2
            if places_total <= 0 or females_total <= 0:
                exit()
        females_total -= 1
    male -= 1
    if places_total <= 0 or males_total <= 0:
        break


