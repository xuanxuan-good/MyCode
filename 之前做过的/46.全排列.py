#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def traceback(nums, level):
            # terminator
            if level == len(nums):
                res.append(nums[:])
                return
            # current logic ; drill down
            for i in range(level, len(nums)):
                nums[level], nums[i] = nums[i], nums[level]
                traceback(nums, level+1)
            # reverse current state
                nums[level], nums[i] = nums[i], nums[level]
        traceback(nums, 0)
        return res
# @lc code=end

