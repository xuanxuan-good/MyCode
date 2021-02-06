#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1.暴力：递归，指数
        # 2.BFS:相当于一棵树，点表示的是amount-coin后的剩余金额，边就是减的不同硬币数；层序遍历到最小为0的叶子节点，层数就是所需的最小个数
        # 3.DP  
        # a.subproblems
        # b.dp array：f(n) = min{f(n-k) (k in [1,2,5])} + 1
        # c.dp方程
        # 一维数组 动态规划
        '''
        dp = [float("inf")] * (amount+1)
        dp[0] = 0  # !!!注意初始赋值
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1
        '''

        dp = [float("inf")] * (amount+1)
        dp[0] = 0  # !!!注意初始赋值
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1
# @lc code=end

