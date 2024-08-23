numbers_of_pages = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())

total_hours_per_day = (numbers_of_pages / pages_per_hour) / days_to_finish

print(int(total_hours_per_day))
