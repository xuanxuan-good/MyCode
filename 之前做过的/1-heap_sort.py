'''
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and nums[child_index+1] > nums[child_index]:
            child_index += 1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    nums[parent_index] = temp
def heap_sort(nums):
    for i in range(len(nums)//2 - 1, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0 ,j, nums)
'''

'''
1. 数组元素依次建立大顶堆
2. 堆顶元素依次放到最后，并删除
从最后一个父节点开始遍历，heapify的过程就是，将左右子结点中，较大的与父节点交换（前提是父节点比子结点小）;
删除后，只有0处的父节点是新交换的元素，所以只需要对0处进行heapify
'''
import heapq
def heap_sort(nums):
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])
    # print(heap)
    for j in range(len(nums)):
        nums[j] = heapq.heappop(heap)

array = [3, 1, 0, 6, 4, 8]
heap_sort(array)
print(array)  # [0, 1, 3, 4, 6, 8]