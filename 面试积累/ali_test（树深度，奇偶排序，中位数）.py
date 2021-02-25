# 树的题怎么测试？
# 树的最大宽度
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

# def maxDepth(root: Node):
#     depth = 0
# 	if not root:
# 		return 0
#     else:
#         for child in root.children:
#             depth = max(depth, maxDepth(child))
# 		return 1 + depth

# roots = Node{val:3, children:Node{val:2}, children:Node{val:1}}  #?
# print(maxDepth(roots))

# 奇偶排序规则的实现
# # 1. 偶数(最后一位是0)排在奇数前面
nums = [3, 4, 5, 8, 6]

# j = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         j += 1

# print(nums, j + 1)
# [4, 8, 6, 3, 5] 4

def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    merge(nums, left, mid, right)
def merge(nums, left, mid, right):
    # 这里比较的规则是当a<b时，a在前，b在后；如果要将奇数在后，偶数在前，也可以设置一种规则将它们放进去
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0
    while i <= mid and j <= right:
        # 设置的规则是：偶数(最后一位是0)排在奇数前面
        # 一奇数一偶数；两偶数，小的放在前边；两奇数，小的在前边；
        if nums[i] & 1 and not nums[j] & 1:  # i奇数，j偶数
            temp[k] = nums[j]
            k += 1
            j += 1
        elif nums[j] & 1 and not nums[i] & 1:  # j奇数，i偶数
            temp[k] = nums[i]
            k += 1
            i += 1
        elif not nums[i] & 1 and not nums[j] & 1:  # ij偶数
            # 也可以随意放进去，只要是偶数就行
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                k += 1
                j += 1
        # elif nums[i] & 1 and nums[j] & 1:  # ij奇数，先跳过，奇数最后放---两次遍历，偶数放好再放奇数
        else:
            i += 1
            j += 1
    while i <= mid:
        if nums[i] % 2 == 0:
            temp[k] = nums[i]
            k += 1
        i += 1
    while j <= right:
        if nums[j] % 2 == 0:
            temp[k] = nums[j]
            k += 1
        j += 1
    # 这只是把偶数放进去了。。。

    if left == 0 and right == len(nums) - 1:
        FirstOddPosition = k
        print(FirstOddPosition)

    i = left
    j = mid + 1
    while i <= mid and j <= right:
        # 再放奇数
        if nums[i] & 1 and not nums[j] & 1:  # i奇数，j偶数
            temp[k] = nums[i]
            k += 1
            i += 1
        elif nums[j] & 1 and not nums[i] & 1:  # j奇数，i偶数
            temp[k] = nums[j]
            k += 1
            j += 1
        elif nums[i] & 1 and nums[j] & 1:  # ij奇数
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                k += 1
                j += 1
        # elif nums[i] & 1 and nums[j] & 1:  # ij奇数，先跳过，奇数最后放---两次遍历，偶数放好再放奇数
        else:
            i += 1
            j += 1
    while i <= mid:
        if nums[i] % 2:
            temp[k] = nums[i]
            k += 1
        i += 1
    while j <= right:
        if nums[j] % 2:
            temp[k] = nums[j]
            k += 1
        j += 1
    nums[left: right + 1] = temp

merge_sort(nums, 0, len(nums) - 1)
print(nums)

'''
# 打印数组中第 3 大的数 heap
# # 除前 10 个大数以外的所有数字   1 2 3 3 1   的中位数 2 (要判断个数奇偶)
# 小顶堆，每次弹出

import heapq
import collections
nums = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 11, 12, 7, 8, 9, 13, 1]

# 统计每个数字出现频次，元素k：次数v
counter = collections.Counter(nums)

# 构造大顶堆，pop出第3个数
heap = [(-k, v) for k, v in counter.items()]
heapq.heapify(heap)
for _ in range(3):
    res = -heapq.heappop(heap)[0]

for _ in range(7):
    heapq.heappop(heap)
arr = []
for key, val in heap:
    # print(key, val)
    arr.extend([-key] * val)
# print(arr)
arr.sort()
if len(arr) % 2 == 0:
    print(res, (arr[len(arr) // 2] + arr[len(arr) // 2]) * 0.5)
else:
    print(res, arr[len(arr) // 2])
'''