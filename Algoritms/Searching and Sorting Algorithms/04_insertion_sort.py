nums = [int(x) for x in input().split()]

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        else: # when the elements ot the left of the number are sorted , no need for more iterations
            break

print(*nums, sep=' ')