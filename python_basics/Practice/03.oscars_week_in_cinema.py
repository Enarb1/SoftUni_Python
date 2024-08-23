movie_title = input()
hall_type = input()
tickets_bought_qty = int(input())


if movie_title == "A Star Is Born":
    if hall_type == "normal":
        ticket_price = 7.50
    elif hall_type == "luxury":
        ticket_price = 10.50
    else:
        ticket_price = 13.50
elif movie_title == "Bohemian Rhapsody":
    if hall_type == "normal":
        ticket_price = 7.35
    elif hall_type == "luxury":
        ticket_price = 9.45
    else:
        ticket_price = 12.75
elif movie_title == "Green Book":
    if hall_type == "normal":
        ticket_price = 8.15
    elif hall_type == "luxury":
        ticket_price = 10.25
    else:
        ticket_price = 13.25
else:
    if hall_type == "normal":
        ticket_price = 8.75
    elif hall_type == "luxury":
        ticket_price = 11.55
    else:
        ticket_price = 13.95

income = ticket_price * tickets_bought_qty

print(f"{movie_title} -> {income:.2f} lv.")