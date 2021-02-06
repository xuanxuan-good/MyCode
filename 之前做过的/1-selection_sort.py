def selection_sort(nums):
    n = len(nums)
    minindex = 0
    for i in range(n):
        minindex = i
        for j in range(i+1, n):
            if nums[j] < nums[minindex]:
                minindex = j
        nums[i], nums[minindex] = nums[minindex], nums[i]
    return nums

nums = [8, 5, 0, 9, 4, 1]
print(selection_sort(nums))  # [0, 1, 4, 5, 8, 9]