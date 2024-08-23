def black_flag(days_pirating, plunder_for_a_day, expected_plunder):
    total_plunder = 0
    for day in range(1, days_pirating + 1):
        total_plunder += plunder_for_a_day
        if day % 3 == 0:
            total_plunder += plunder_for_a_day * 0.5
        if day % 5 == 0:
            total_plunder -= 0.3 * total_plunder

    if total_plunder >= expected_plunder:
        return f"Ahoy! {total_plunder:.2f} plunder gained."
    else:
        plunder_gained = (total_plunder / expected_plunder) * 100
        return f"Collected only {plunder_gained:.2f}% of the plunder."


days_pirating = int(input())
plunder_for_a_day = int(input())
expected_plunder = float(input())

print(black_flag(days_pirating,plunder_for_a_day,expected_plunder))
