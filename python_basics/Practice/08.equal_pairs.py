pairs = int(input())
max_diff = 0
previous_sum = None

for _ in range(pairs):
    n1 = int(input())
    n2 = int(input())
    pair_sum = n1 + n2

    if previous_sum is not None:
        diff = abs(pair_sum - previous_sum)
        if diff > max_diff:
            max_diff = diff

        previous_sum = pair_sum
    else:
        previous_sum = pair_sum

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")
