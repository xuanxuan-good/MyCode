#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #半升序，二分的话一定有一半的数组是有序的
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:  # 等于号?  [3,-1]
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

'''
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else: r = mid - 1
            else:
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid - 1
                else: l = mid
        if nums[r] == target:
            return r
        return -1
'''
# @lc code=end

