def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx

        for currents_idx in range(idx + 1 , len(nums)):
            if nums[currents_idx] < nums[min_idx]:
                min_idx = currents_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]


numbers = [int(x) for x in input().split()]
selection_sort(numbers)
print(*numbers)
