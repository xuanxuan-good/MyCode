# 类似题：[剑指 Offer 53 - I. 在排序数组中查找数字 I]（统计数字在排序数组中出现的次数）
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 进阶：
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]

# 示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
 

# 提示：
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 是一个非递减数组
# -109 <= target <= 109

# 剑指 Offer 53 - I. 在排序数组中查找数字 I 【同理，只不过返回值是这个重复数字的长度】

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        if not nums: return [-1, -1]
        left = self.search(nums, target, True)
        right = self.search(nums, target, False) - 1
        if left <= right < len(nums) and nums[left] == nums[right] == target:
            return [left, right]
        return [-1, -1]

    def search(self, nums, target, flag):
        # 答案应该可以取到len(nums), 比如[1] 1 这种情况-->r=1,第一个比1大的值在范围外
        l, r = 0, len(nums)
        while l < r:
            mid = l + r >> 1
            if nums[mid] > target or (flag and nums[mid] >= target):
                r = mid
            else: l = mid + 1
        return r
# @lc code=end

