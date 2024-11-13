def binary_search(arr, target):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_el = arr[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return -1



nums = [int(x) for x in input().split()]
target_num = int(input())


print(binary_search(nums, target_num))