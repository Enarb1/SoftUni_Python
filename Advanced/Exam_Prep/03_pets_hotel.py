def accommodate_new_pets(hotel_capacity, max_weight_allowed,*pets):
    pets_in_hotel = {}
    final_print = ""

    for pet_type, pet_weight in pets:
        if hotel_capacity <= 0:
            final_print += "You did not manage to accommodate all pets!\n"
            break
        if pet_weight > max_weight_allowed:
            continue
        else:
            pets_in_hotel[pet_type] = pets_in_hotel.get(pet_type, 0) + 1
            hotel_capacity -= 1
    else:
       final_print += f"All pets are accommodated! Available capacity: {hotel_capacity}.\n"


    final_print += "Accommodated pets:\n"
    for pet, count in sorted(pets_in_hotel.items()):
       final_print += f"{pet}: {count}\n"

    return final_print