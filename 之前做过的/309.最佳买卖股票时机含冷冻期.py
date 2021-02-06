#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1.动态规划，f[n][3]持有股票非冷冻期f[i][0];不持有股票冷冻期f[i][1];不持有股票非冷冻期f[i][2]
        # 第i天持有股票 f[i][0]=max(f[i-1][0],f[i-1][2]-price[i])
        # 第i天不持有股票冷冻期 f[i][1]=f[i-1][0]+price[i]  表示在第i天结束之后处于冷冻期，也就是当天卖出了股票
        # 第i天不持有股票非冷冻期 f[i][2]=max(f[i-1][1],f[i-1][2])  如果前一天卖出，今天应该处于冷冻期
        # f[0][0]=-price[0], f[0][1]=f[0][2]=0
        # return f[-1][1]和f[-1][2]中最大值 ; 因为最后一天手里持有股票没有任何意义

        # 2.动态规划，空间优化  理解：1表示下一天会处于冷冻期，因此这一天之后不能卖股票
        # dp0=-price[0],dp1=dp2=0
        # 持有股票非冷冻期dp0=max(dp0,dp2-price[i])
        # 不持有股票冷冻期dp1=dp0+price[i]
        # 不持有股票非冷冻期dp2=max(dp2,dp1)
        if not prices:
            return 0
        # 持有股票非冷冻期dp0 ； 不持有股票冷冻期dp1 ； 不持有股票非冷冻期dp2
        dp0 = -prices[0]
        dp1 = dp2 = 0
        for i in range(len(prices)):
            dp0, dp1, dp2 = max(dp0, dp2-prices[i]), dp0+prices[i], max(dp2,dp1)
        return max(dp1, dp2)
# @lc code=end

