def accommodate(*guests, **rooms):

    sorted_rooms = sorted(rooms.items(), key=lambda kvp: (kvp[1], kvp[0]))
    occupied_rooms = {}
    total_guest = sum(guests)

    for guest in guests:
        for room_n, capacity in sorted_rooms:
            if room_n not in occupied_rooms.keys():
                if capacity == guest:
                    occupied_rooms[room_n] = guest
                    break
                elif capacity > guest:
                    occupied_rooms[room_n] = guest
                    break

    accommodated_guests = sum(x for x in occupied_rooms.values())
    occupied_rooms = sorted(occupied_rooms.items(), key=lambda kvp: kvp[0])
    message = ''
    if occupied_rooms:
        message += f"A total of {len(occupied_rooms)} accommodations were completed!\n"
        for room_num, guest_count in occupied_rooms:
            message += f"<Room {room_num[5:]} accommodates {guest_count} guests>\n"
    else:
        message += "No accommodations were completed!\n"

    if total_guest - accommodated_guests != 0:
        message += f"Guests with no accommodation: {total_guest - accommodated_guests}\n"
    if len(occupied_rooms) != len(rooms):
        message += f"Empty rooms: {len(rooms) - len(occupied_rooms)}"

    return message