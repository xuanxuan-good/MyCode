#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp 或 贪心
        if not prices:
            return 0
        dp0, dp1 = 0, -prices[0]
        for price in prices[1:]:
            dp0, dp1 = max(dp0, dp1+price-fee), max(dp1,dp0-price)
        return max(dp0, dp1)
# @lc code=end

