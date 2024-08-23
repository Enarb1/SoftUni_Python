odd_nums = set()
even_nums = set()

for row in range(1, int(input()) + 1):
    result = int((sum(ord(char) for char in input())) / row)
    if result % 2 == 0:
        even_nums.add(result)
    else:
        odd_nums.add(result)

sum_odd_set, sum_even_set = sum(odd_nums), sum(even_nums)

if sum_odd_set == sum_even_set:
    print(*odd_nums.union(even_nums), sep=', ')
elif sum_odd_set > sum_even_set:
    print(*odd_nums.difference(even_nums), sep=', ')
elif sum_odd_set < sum_even_set:
    print(*odd_nums.symmetric_difference(even_nums), sep=', ')
