#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，
# 每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
# 返回区域的数目。


# 示例 1：
# 输入：
# [
#   " /",
#   "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：

# 示例 2：
# 输入：
# [
#   " /",
#   "  "
# ]
# 输出：1
# 解释：2x2 网格如下：

# 示例 3：
# 输入：
# [
#   "\\/",
#   "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
 

# 提示：
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。

# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        '''
        另一种非递归的压缩方法
        '''
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        '''
           0
        3     1
           2
        '''
        n = len(grid)
        size = 4 * n * n
        uf = UnionFind(size)
        for i in range(n):
            row = list(grid[i])
            for j in range(n):
                c = row[j]
                index = 4 * (i * n + j)
                if c == '/':
                    uf.union(index, index + 3)
                    uf.union(index + 1, index + 2)
                elif c == '\\':
                    uf.union(index, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)

                if j + 1 < n:
                    uf.union(index + 1, 4 * (i * n + j + 1) + 3)
                if i + 1 < n:
                    uf.union(index + 2, 4 * ((i + 1) * n + j))
        return uf.getCount()
# @lc code=end

