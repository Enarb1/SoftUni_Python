deposit = int(input())
duration_months = int(input())
percent = float(input())

total_sum = deposit + duration_months * ((deposit *(percent / 100))/12)

print(total_sum)
