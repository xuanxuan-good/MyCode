#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1.递归dfs，当前是哪一天index，是买入1还是卖出0status，是交易的第几次k
        # 如果是买入，则保持不动或者卖出；如果是卖出，则保持不动或者立马再买 同时count加一
        # dfs(index+1;0/1;k[+1])+/- price[index]

        # 2.递归+记忆化，用一个哈希表缓存重复的调用

        # 3.动态规划【索引设置上有点绕】，三维数组dp[i][0,1,2][0,1] 第几天，第几次，卖出还是买入
        # dp[0][0][0]=dp[0][1][0]=dp[0][2][0]=0; dp[0][0][1]=dp[0][1][1]=dp[0][2][1]=-price[0]
        # 第i天，0次交易，卖出dp[i][0][0]=dp[i-1][0][0]
        # 第i天，一次交易，买入dp[i][0][1]=max(dp[i-1][0][1],dp[i-1][0][0]-price[index]),第i天，一次交易，卖出dp[i][1][0]=max(dp[i-1][1][0],dp[i-1][0][1]+price[index])
        # 第i天，第二次交易，买入dp[i][1][1]=max(dp[i-1][1][1],dp[i-1][1][0]-price[index]),第i天，第二次交易，卖出dp[i][2][0]=max(dp[i-1][2][0],dp[i-1][1][1]-price[index])
        # return 5个值中的最大值  [也可以设置买入时 加k值]

        # 4.动态规划，二维数组，五种不同的状态，初始，买入卖出1，买入卖出2。
        # dp[n][5],dp[0][0]=dp[0][2]=dp[0][4]=0; dp[0][1]=dp[0][3]=-price[0]
        # dp[i][0]=0 ; dp[i][1]=max(dp[i-1][1],dp[i-1][0]-price[i]); dp[i][2]=max(dp[i-1][2],dp[i-1][1]+price[i])
        # dp[i][3]=max(dp[i-1][3],dp[i-1][2]-price[i]); dp[i][4]=max(dp[i-1][4],dp[i-1][3]+price[i])
        # return dp[-1][5] 5个值中的最大值

        # √5.动态规划，空间优化，每次只需要当前状态和前一个状态的值 初始，入出1，入出2
        # dp0 = dp2 = dp4 = 0;dp1 = dp3 = -price[0]
        # dp1=max(dp1,dp0-price[i]), dp2=max(dp2,dp1+price[i]), dp3=max(dp3,dp2-price[i]), dp4=max(dp4, dp3+price[i])
        # 取五个值中最大值
        if not prices:
            return 0
        # 0初始1买入2卖出3买入4卖出
        dp0 = dp2 = dp4 = 0
        dp1 = dp3 = -prices[0]
        for i in range(len(prices)):
            dp1 = max(dp1, dp0-prices[i])
            dp2 = max(dp2, dp1+prices[i])
            dp3 = max(dp3, dp2-prices[i])
            dp4 = max(dp4, dp3+prices[i])
        return max(dp0, dp1, dp2, dp3, dp4)
# @lc code=end

