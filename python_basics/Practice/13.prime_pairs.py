first_pair_start = int(input())
second_pair_start = int(input())
limit_first_pair = int(input())
limit_second_pair = int(input())

for first_nums in range(first_pair_start, first_pair_start + limit_first_pair + 1):
    for second_nums in range(second_pair_start, second_pair_start + limit_second_pair + 1):
        is_prime_first_pair = True
        is_prime_second_pair = True
        for x in range(2, int(first_nums**0.5) + 1):
            if first_nums % x == 0:
                is_prime_first_pair = False
                break
        for y in range(2, int(second_nums ** 0.5) + 1):
            if second_nums % y == 0:
                is_prime_second_pair = False
                break
        if is_prime_first_pair and is_prime_second_pair:
            print(f"{first_nums}{second_nums}")







