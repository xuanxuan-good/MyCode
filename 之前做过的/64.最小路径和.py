#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j != 0:
                    grid[0][j] += grid[0][j-1]
                if j == 0 and i != 0:
                    grid[i][0] += grid[i-1][0]
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

