def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)
def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left: right + 1] = temp

array = [1, 5, 3, 7, 0]
left, right = 0, len(array) - 1
merge_sort(array, left, right)
print(array)  # [0, 1, 3, 5, 7]