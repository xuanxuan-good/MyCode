#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # 优化
        if not prices:
            return 0
        dp0, dp1 = 0, -prices[0]
        for price in prices:
            dp0, dp1 = max(dp0, dp1+price), max(dp1, -price)
        return dp0
        '''
        # dp[i][01]
        if not prices:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(0-prices[i], dp[i-1][1])  # dp[i-1][0]=0,不应该直接加进去，因为k=1
        return dp[-1][0]
        '''
# @lc code=end

