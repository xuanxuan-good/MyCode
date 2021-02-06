#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 相当于围成了一圈，第一个房屋和最后一个房屋不能同时偷，所以nums[1:]和nums[:-1]中能偷的最大值就是最终结果
        def my_rob(nums):
            pre, now = 0, 0
            for num in nums:
                pre, now = now, max(pre+num, now)
            return now
        return max(my_rob(nums[1:]), my_rob(nums[:-1])) if len(nums) != 1 else nums[0]
# @lc code=end

