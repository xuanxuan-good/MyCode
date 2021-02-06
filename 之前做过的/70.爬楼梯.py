#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        '''
        爬楼梯问题变形：
            1.可以走1，2，3步--状态转移方程变为dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
            2.可以走一个数组里的任意m步--多加一个循环条件，for j in range(m):  dp[i] += dp[i-x[j]]
            3.不能走相同的步数--状态转移方程多加一个维度，dp[i][k] ,多加一个循环条件，for k in range(m):  dp[i][k] += dp[i][!k]
        '''
        first, second = 0, 1
        for _ in range(1, n+1):
            res = first + second
            first = second
            second = res
        return res
        '''
        if n < 3:
            return n
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        '''

        '''
        if n < 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
# @lc code=end

