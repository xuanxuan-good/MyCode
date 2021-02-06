#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp, 含有‘1’的最大正方形的面积---三个方向取最小
        if not matrix or len(matrix) < 1:
            return 0
        row, col = len(matrix), len(matrix[0])
        maxslide = 0
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':  # 当前位置的左，上，左上
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1  # 注意索引
                    maxslide = max(maxslide, dp[i+1][j+1])
        return maxslide * maxslide
# @lc code=end

