#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 优化
        if not nums:
            return 0
        dp0, dp1 = 0, nums[0]
        for i in range(1, len(nums)):
            dp0, dp1 = max(dp0, dp1), dp0 + nums[i]
        return max(dp0, dp1)
        '''
        # dp[i][01]
        if not nums:
            return 0
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])
        '''
# @lc code=end

