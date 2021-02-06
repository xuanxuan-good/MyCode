#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 枚举所有的起点和终点 O(n^2)
        # dp 最大子序和 = 当前元素自身最大，或者 包含之前后最大
        # dp问题，公式为：dp[i] = max(nums[i], nums[i]+dp[i-1])
        # 1.分治（子问题） max_sum(i) = max(max_sum(i-1), 0) + a[i]
        # 2.状态数组定义： f[i]
        # 3.DP方程：f[i] = max(f[i-1],0)+a[i]
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            # dp[i] = nums[i] + max(0, dp[i-1])
        return max(dp)
        '''
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
        '''
        
        '''
        # 贪心  如果之前的和是小于零的，就舍弃
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum+nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum
        '''
# @lc code=end

