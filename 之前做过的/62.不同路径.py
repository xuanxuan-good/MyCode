#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 优化
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
        '''
        # 递推
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        '''

        '''
        # 递归优化  37/62
        mem = {}
        if m <= 0 or n <= 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if (m, n) not in mem:
            mem[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return mem[(m, n)]
        '''

        '''
        # 递归  37/62
        if m <= 0 or n <= 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        '''
# @lc code=end

