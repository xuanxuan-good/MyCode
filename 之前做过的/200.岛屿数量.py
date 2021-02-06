#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        count, space = row*col, 0
        p = [i for i in range(row * col)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    for x, y in [[1, 0], [0, -1]]:  # 向右向下遍历，符合条件就进行合并
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                            a = self.union(p, tmp_i * col + tmp_j, i * col + j)
                            if a != 1:
                                count -= 1  # 只要发生过合并，岛屿的数量就减少一
                else:
                    space += 1  # 记录空地数量
        return count - space  # 连通分量个数减空地个数

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        if p1 == p2:  #增加的
            return 1
        p[p2] = p1

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i; i = p[i]; p[x] = root
        return root
        '''
        # dfs
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return 
        grid[i][j] = True
        for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.dfs(grid, i+r, j+c)
        '''
# @lc code=end

