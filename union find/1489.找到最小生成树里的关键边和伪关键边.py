#
# @lc app=leetcode.cn id=1489 lang=python3
#
# [1489] 找到最小生成树里的关键边和伪关键边
# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。
# 最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。

# 请你找到给定图中最小生成树的所有关键边和伪关键边。
# 如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
# 伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。

# 请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。


# 示例 1：
# 输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]

# 示例 2 ：
# 输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
 

# 提示：
# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# 所有 (fromi, toi) 数对都是互不相同的。


# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.setCount = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_x] += self.size[root_y]
        self.setCount -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal 算法
        m = len(edges)
        # 在列表的列表中加入序号的方法
        for i, edge in enumerate(edges):
            edge.append(i)

        # 构建最小生成树，并计算最小权值
        edges.sort(key = lambda x:x[2])
        uf_std = UnionFind(n)
        value = 0
        for edge in edges:
            if uf_std.union(edge[0], edge[1]):
                value += edge[2]

        # 关键边也满足伪关键边的性质，因此先判断关键边
        ans = [list(), list()]
        for i in range(m):
            uf = UnionFind(n)
            v = 0
            # 如果去掉i这条边之后，用其他的边生成最小生成树；
            # 如果整个图不连通，则不存在最小生成树；整个图连通（连通数为1）并且最小生成树的权值大于value--->关键边
            ### 为什么要整个图连通才能生成最小生成树？？？
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                ans[0].append(edges[i][3])
                continue

            # 伪关键边：可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
            # 也就是说，我们可以在计算最小生成树的过程中，最先考虑这条边i，即'最先将这条边的两个端点在并查集中合并'
            # 设最终得到的最小生成树权值为 v，如果 v = value，那么这条边就是伪关键边。（可有可无）
            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.union(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                ans[1].append(edges[i][3])

        return ans
# @lc code=end

