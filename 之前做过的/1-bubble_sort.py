'''
冒泡的时间复杂度是O(n^2),最好情况下是O(n),即数组中的数是正序的
'''

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

'''
# 1.外层优化，不发生交换就停止循环
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        flag = True
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = False
        if flag:
            break
    return nums
'''

'''
# 2.内层优化，每次记录最后交换的位置，减少循环次数
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        pos = i
        for j in range(n-pos-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                pos = j
    return nums
'''

nums = [8, 5, 0, 9, 4, 1]
print(bubble_sort(nums))  # [0, 1, 4, 5, 8, 9]