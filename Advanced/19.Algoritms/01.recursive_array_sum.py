def recursive_sum(numbers, idx=0):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + recursive_sum(numbers, idx + 1)


nums = [int(n) for n in input().split()]
print(recursive_sum(nums))
