team = input() #Argentina", "Brazil", "Croatia", "Denmark
souvenier = input()  # "flags", "caps", "posters", "stickers"
qty_souvenier = int(input())

flags_price = 0
caps_price = 0
posters_price = 0
stickers_price = 0
total_price = 0

if team == "Argentina":
    if souvenier == "flags":
        flags_price = 3.25
        total_price = flags_price * qty_souvenier
    elif souvenier == "caps":
        caps_price = 7.20
        total_price = caps_price * qty_souvenier
    elif souvenier == "posters":
        posters_price = 5.10
        total_price = posters_price * qty_souvenier
    elif souvenier == "stickers":
        stickers_price = 1.25
        total_price = stickers_price * qty_souvenier
    else:
        print("Invalid stock!")
        exit()

elif team == "Brazil":
    if souvenier == "flags":
        flags_price = 4.20
        total_price = flags_price * qty_souvenier
    elif souvenier == "caps":
        caps_price = 8.50
        total_price = caps_price * qty_souvenier
    elif souvenier == "posters":
        posters_price = 5.35
        total_price = posters_price * qty_souvenier
    elif souvenier == "stickers":
        stickers_price = 1.20
        total_price = stickers_price * qty_souvenier
    else:
        print("Invalid stock!")
        exit()
elif team == "Croatia":
    if souvenier == "flags":
        flags_price = 2.75
        total_price = flags_price * qty_souvenier
    elif souvenier == "caps":
        caps_price = 6.90
        total_price = caps_price * qty_souvenier
    elif souvenier == "posters":
        posters_price = 4.95
        total_price = posters_price * qty_souvenier
    elif souvenier == "stickers":
        stickers_price = 1.10
        total_price = stickers_price * qty_souvenier
    else:
        print("Invalid stock!")
        exit()
elif team == "Denmark":
    if souvenier == "flags":
        flags_price = 3.10
        total_price = flags_price * qty_souvenier
    elif souvenier == "caps":
        caps_price = 6.50
        total_price = caps_price * qty_souvenier
    elif souvenier == "posters":
        posters_price = 4.80
        total_price = posters_price * qty_souvenier
    elif souvenier == "stickers":
        stickers_price = 0.90
        total_price = stickers_price * qty_souvenier
    else:
        print("Invalid stock!")
        exit()
else:
    print("Invalid country!")
    exit()


print(f"Pepi bought {qty_souvenier} {souvenier} of {team} for {total_price:.2f} lv.")

