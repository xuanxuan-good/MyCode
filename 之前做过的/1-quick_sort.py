'''
双指针实现快排？
'''

# 从头到尾遍历数组，大的放在pivot右边，小的放在pivot左边
def quick_sort(begin, end, nums):
    if begin >= end :
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[mark], nums[begin] = nums[begin], nums[mark]
    return mark

array = [3, 1, 6, 2, 9]
end = len(array)-1  # 最后位置的索引
quick_sort(0, end, array)
print(array)  # [1, 2, 3, 6, 9]