#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 5.dp 自底向上 原地 O(n^2) O(1)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        
        '''
        # 6.dp 自底向上 O(n^2) O(n)
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]
        '''

        '''
        # 4.dp 自顶向下 优化 O(n^2) O(n)
        n = len(triangle)
        res = [0] * n
        res[0] = triangle[0][0]
        for i in range(1, n):
            res[i] = res[i-1] + triangle[i][i]
            for j in range(i-1, 0, -1):
                res[j] = min(res[j], res[j-1]) + triangle[i][j]
            res[0] += triangle[i][0]
        return min(res)
        '''

        '''
        # 3.dp 自顶向下 O(n^2) O(n^2) loopi 1-n dpi0=dp[i-1][0]+ti0 loopj 1--i-1 dpii=dp[i-1][i-1]+tii dpij=min(dp[i-1][j], dp[i-1][j-1])+tij  
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        return min(dp[-1])
        '''

        '''
        # 2.递归+记忆化
        n = len(triangle)
        memo = [[0]*n for _ in range(n)]
        return self.dfs(memo, triangle, 0, 0)
    def dfs(self, memo, triangle, i, j):
        if i == len(triangle):
            return 0
        if memo[i][j] != 0:
            return memo[i][j]
        memo[i][j] = min(self.dfs(memo, triangle, i+1, j), self.dfs(memo, triangle, i+1, j+1)) + triangle[i][j]
        return memo[i][j]
        '''

        '''
        # 1.递归 自顶向下
        return self.dfs(triangle, 0, 0)
    def dfs(self, triangle, i, j):
        if i == len(triangle):
            return 0
        return min(self.dfs(triangle, i+1, j), self.dfs(triangle, i+1, j+1)) + triangle[i][j]
        '''
# @lc code=end

