#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。

# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2

# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1

# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4

# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        因为答案可能取到len(nums),这时取r = len(nums)
        # bisect  如果没找到这个值，返回右边第一个比它大的索引；；如果找到这个值，返回这个值右侧的索引
        # bisect_left  如果没找到这个值，返回右边第一个比它大的索引；；如果找到这个值，'返回这个值'
        '''
        l, r = 0, len(nums)
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid
            else: l = mid + 1
        return r

        # return bisect.bisect_left(nums, target)
# @lc code=end

