#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 最多可以完成k笔交易--dp
        # 1.if k >= len/2--因为一次需要两天，所以相当于没有限制  时空复杂度O（NK）长度乘交易次数
        # dp[][][] 第i天len+1，交易次数k+1，是否持股2  不持股初值设置为0，持股设置为较小的负值
        # dp[i][j][1]=max(dp[i-1][j-1][0]-price[i], dp[i-1][j][1])  因为从1到len+1遍历
        # dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+price[i])
        # return dp[len][k][0]

        # 2.dp[k+1][2] k>len/2 无限制  初值-不持股0；持股负值 时空复杂度O（NK）长度乘交易次数
        # loop price:prices  loop j 1-k+1
        # dp[j][1]=max(dp[j-1][0]-price,dp[j][1])
        # dp[j][0]=max(dp[j][0],dp[j][1]+price)
        # return dp[k][0]

        if not prices:
            return 0
        if k > len(prices)//2:
            return sum(x-y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        dp = [[0, 0] for _ in range(k+1)]
        for i in range(k+1):
            dp[i][1] = -prices[0]  # 在没有进行股票交易时不允许持有股票
        for price in prices:
            for j in range(1, k+1):  # 边界还是需要注意 2020.12.29
                dp[j][0] = max(dp[j][0], dp[j][1]+price)
                dp[j][1] = max(dp[j][1], dp[j-1][0]-price)  # 每次买入操作会使用一次交易
        return dp[-1][0]  #结束时持有 0 份股票的收益一定大于持有 1 份股票的收益。

        '''
        if k >= len(prices) // 2:
            return sum(x-y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]
        for j in range(1, k+1):
            dp[0][j][1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]
        '''
# @lc code=end

