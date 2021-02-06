#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:  #48ms 73%
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                if i != j:
                    nums[j] =nums[i]
        return j+1
# @lc code=end

