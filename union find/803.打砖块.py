#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
# 有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：
# 一块砖直接连接到网格的顶部，或者至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
# 给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。
# 一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

# 返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。
# 注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

# 示例 ：
# 输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 网格开始为：
# [[1,0,0,0],
#  [1,1,0,0]]
# 消除 (1,1) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [1,0,0,0]]
# 剩下的砖都很稳定，所以不会掉落。网格保持不变：
# [[1,0,0,0], 
#  [1,0,0,0]]
# 接下来消除 (1,0) 处加粗的砖块，得到网格：
# [[1,0,0,0],
#  [0,0,0,0]]
# 剩下的砖块仍然是稳定的，所以不会有砖块掉落。
# 因此，结果为 [0,0] 。
 

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] 为 0 或 1
# 1 <= hits.length <= 4 * 104
# hits[i].length == 2
# 0 <= xi <= m - 1
# 0 <= yi <= n - 1
# 所有 (xi, yi) 互不相同

# @lc code=start
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        # 二维坐标转换为一维坐标
        def getIndex(x, y):
            return x * cols + y

        # 输入坐标在二维网格中是否越界
        def inArea(x, y):
            return 0 <= x < rows and 0 <= y < cols

        # 第 1 步：把 grid 中的砖头全部击碎，通常算法问题不能修改输入数据，这一步非必需，可以认为是一种答题规范
        copy = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                copy[i][j] = grid[i][j]

        # 把 copy 中的砖头全部击碎
        for hit1, hit2 in hits:
            copy[hit1][hit2] = 0

        # 第 2 步：建图，把砖块和砖块的连接关系输入并查集，size 表示二维网格的大小，也表示虚拟的「屋顶」在并查集中的编号
        size = rows * cols
        uf = UnionFind(size + 1)

        # 将下标为 0 的这一行的砖块与「屋顶」相连
        for j in range(cols):
            if copy[0][j] == 1:
                uf.union(j, size)

        # 其余网格，如果是砖块向上、向左看一下，如果也是砖块，在并查集中进行合并 !!!
        for i in range(1, rows):
            for j in range(cols):
                if copy[i][j] == 1:
                    # 如果上边也是砖块
                    if copy[i - 1][j] == 1:
                        uf.union(getIndex(i - 1, j), getIndex(i, j))
                    # 如果左边也是砖块
                    if j > 0 and copy[i][j - 1] == 1:
                        uf.union(getIndex(i, j - 1), getIndex(i, j))

        # 第 3 步：按照 hits 的逆序，在 copy 中补回砖块，把每一次因为补回砖块而与屋顶相连的砖块的增量记录到 res 数组中
        hitsLen = len(hits)
        res = []
        for x, y in reversed(hits):
            if grid[x][y] == 0:
                res.append(0)
                continue
            
            # 补回之前与屋顶相连的砖块数
            origin = uf.getSize(size)

            # 注意：如果补回的这个结点在第 1 行，要告诉并查集它与屋顶相连（逻辑同第 2 步）
            if x == 0:
                uf.union(y, size)

            # 在 4 个方向上看一下，如果相邻的 4 个方向有砖块，合并它们
            for i in range(4):
                newX, newY = x + dx[i], y + dy[i]

                if inArea(newX, newY) and copy[newX][newY] == 1:
                    uf.union(getIndex(newX, newY), getIndex(x, y))

            # 补回之后与屋顶相连的砖块数
            current = uf.getSize(size)
            
            # 减去的 1 是逆向补回的砖块（正向移除的砖块），与 0 比较大小，是因为存在一种情况，添加当前砖块，不会使得与屋顶连接的砖块数更多
            res.append(max(0, current - origin - 1))

            # 真正补上这个砖块
            copy[x][y] = 1

        return res[::-1]


class UnionFind:
    def __init__(self, n):
        '''
        parent:当前结点的父亲结点
        size:以当前结点为根结点的子树的结点总数
        '''
        self.parent = list(range(n))
        self.size = [1] * n

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = rootY
        # 在合并的时候维护数组 size
        self.size[rootY] += self.size[rootX]

    def find(self, x):
        '''
        路径压缩，只要求每个不相交集合的「根结点」的子树包含的结点总数数值正确即可，因此在路径压缩的过程中不用维护数组 size
        '''
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def getSize(self, x):
        '''
        在并查集的根结点的子树包含的结点总数
        :param x
        :return x 在并查集的根结点的子树包含的结点总数
        '''
        root = self.find(x)
        return self.size[root]

# @lc code=end

