#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示包含nums[i]的最长上升子序列的长度;不一定是连续的
        dp = [1] * len(nums)
        res = []
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        '''
        res = []
        inde = dp.index(max(dp))
        res.append(nums[inde])
        for i in range(inde, -1, -1):
            if nums[i] < res[-1]:
                res.append(nums[i])
        print(res[::-1])  # [2, 3, 7, 101]
        '''
        return max(dp)
# @lc code=end

