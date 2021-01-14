#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#在本问题中, 树指的是一个连通且无环的无向图。
# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

# 示例 1：
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的无向图为:
#   1
#  / \
# 2 - 3

# 示例 2：
# 输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# 输出: [1,4]
# 解释: 给定的无向图为:
# 5 - 1 - 2
#     |   |
#     4 - 3

# 注意:
# 输入的二维数组大小在 3 到 1000。
# 二维数组中的整数在1到N之间，其中N是输入数组的大小。

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        并查集(合并和查找根节点)，dfs,bfs,拓扑（深度，广度）
        树的边数量比节点数量少一，这道题在树的基础上多了一条附加的边，因此边和节点数量相同
        树是一个连通且无环的无向图，在树中多加一条附加的边后就会出现环，附加的边就是导致环出现的环
        通过并查集查找附加的边：
        1.遍历每一条边，判断这条边连接的'两个顶点'，如果不属于同一个根节点--则表明在遍历到当前边之前，两个顶点是没有公共根节点的，因此当前边不会导致环的出现，将两个顶点进行合并
        2.如果属于同一个根节点--则表明在遍历到当前边之前，两个顶点是有公共根节点的，因此当前边会导致环的出现，当前边作为答案返回

        时间复杂度：O(NlogN)
            N是图中的节点个数。对每条边的两个节点查找祖先，不同则需要合并；因此需要进行2N次查找和最多N次合并，总时间复杂度O(2NlogN)
            使用了路径压缩，没有使用按秩合并，最坏情况下时间复杂度O(NlogN)，平均情况是O(Nα(N)),α是阿克曼函数的反函数，α(N)可以认为是一个很小的常数。
        空间复杂度：O(N)
            N是图中的节点个数。使用数组parent记录每个节点的祖先
        '''
        nodesCount = len(edges)
        self.parent = list(range(nodesCount + 1))
        
        for node1, node2 in edges:
            if self.find(node1) != self.find(node2):
                self.union(node1, node2)
            else:
                return [node1, node2]
        return []
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_x] = root_y
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]     
# @lc code=end

