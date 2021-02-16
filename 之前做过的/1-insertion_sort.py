def insertion_sort(nums):
    for i in range(1, len(nums)):
        preIndex = i - 1
        current = nums[i]
        while preIndex >= 0 and nums[preIndex] > current:
            nums[preIndex+1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex+1] = current
    return nums

nums = [8, 5, 0, 9, 4, 1]
print(insertion_sort(nums))  # [0, 1, 4, 5, 8, 9]