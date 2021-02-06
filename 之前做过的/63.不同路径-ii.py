#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        1.dp[m][n] 正推
        dp[0][1..j] == 1 if grid[0][j]==0 else break
        dp[1..i][0] == 1 if grid[i][0]==0 else break
        dp[i][j] = 0 if  grid[i][0]==1 dp[i-1][j] + dp[i][j-1] 
        2.dp[n] 逆推
        dp[0] = 1 if grid[0][0] == 0 else 0
        dp[j] = 0 if grid[i][j] == 1
        dp[j] += dp[j-1] if j > 0 and grid[i][j] == 0
        '''
        # 优化 逆推
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0 and obstacleGrid[i][j] == 0:
                    dp[j] += dp[j-1]
        return dp[-1]
        '''
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            if obstacleGrid[i][0] == 1:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            if obstacleGrid[0][j] == 1:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        '''
# @lc code=end

