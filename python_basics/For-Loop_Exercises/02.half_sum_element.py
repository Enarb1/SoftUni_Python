n = int(input())

max_num = float('-inf')
sum_num = 0

for _ in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_num += num
half_sum = sum_num - max_num
if max_num == sum_num - max_num:
    print(f'Yes\nSum = {max_num}')
else:
    print(f"No\nDiff = {abs(max_num - half_sum)}")