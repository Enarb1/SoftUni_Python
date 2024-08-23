numbers = tuple([float(n) for n in input().split()])

occurrences = {}

for num in numbers:
    occurrences[num] = numbers.count(num)

for number, count in occurrences.items():
    print(f'{number:.1f} - {count} times')
