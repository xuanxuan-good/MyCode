#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log n)二分查找，第一个位置索引leftidx就是 数组中第一个大于等于target的下标；
        #                  最后一个位置素银rightidx就是 数组中第一个大于target的下标（再减一即可）
        leftIdx = self.binarySearch(nums, target, True)
        rightIdx = self.binarySearch(nums, target, False) - 1
        if leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
            return [leftIdx, rightIdx]
        return [-1, -1]

    def binarySearch(self, nums, target, lower):
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# @lc code=end

