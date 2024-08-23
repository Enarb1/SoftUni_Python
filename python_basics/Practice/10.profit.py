one_lv = int(input())
two_lv = int(input())
five_lv = int(input())
target_sum = int(input())

for one_lv_count in range(one_lv + 1):
    for two_lv_count in range (two_lv + 1):
        for five_lv_count in range(five_lv + 1):
            current_sum = one_lv_count * 1 + two_lv_count * 2 + five_lv_count * 5
            if current_sum == target_sum:
                print(f"{one_lv_count} * 1 lv. + {two_lv_count} * 2 lv. + {five_lv_count} * 5 lv. = {target_sum} lv.")