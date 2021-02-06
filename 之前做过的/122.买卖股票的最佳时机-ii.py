#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2.回溯，树
        # 1.动态规划 dp[i][0-1]手里有无股票的最大利润 [数组或值--一个值的情况。。。]
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i]) 当前手里没有股票，上一次也没有，或者上一次有但是这一次卖出去了
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price[i]) 当前手里有股票，上一次也有，或者上一次没有 则要减掉这次买股票的price
        '''
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])  # 没有股票
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return max(dp[-1][0], dp[-1][1])
        '''
        # 1.当前没有股票dp0，则上一次也没有股票 或者 上一次有股票+price[i]--买出去了  的最大值
        # 当前有股票dp1，则上一次有股票 或者 上一次没有股票-price[i]--购入了  的最大值
        dp0, dp1 = 0, -prices[0]
        for i in range(len(prices)):
            dp0, dp1 = max(dp0, dp1+prices[i]), max(dp1, dp0-prices[i])
        return dp0
        '''
        # 2.贪心
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i]-prices[i-1])
        return res
        '''
# @lc code=end

