#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

# 示例 ：
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。

# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
 

# 提示：
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10^4
# 不会有两块石头放在同一个坐标点上

# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        如果两个石头，横坐标相等或者纵坐标相等，在它们之间形成一条边
        最多可以移除的石头的个数 = 所有石头的个数 - 连通分量的个数。
        题目没有让我们给出具体移除石头的方案，可以考虑使用并查集。
        删到最后，留在图中的顶点一定位于不同的行和不同的列。因此，并查集里的元素是 描述「横坐标」和「纵坐标」的数值。
        「合并」的语义是：所有横坐标为 x 的石头和所有纵坐标为 y 的石头都属于同一个连通分量。--> 将每个 stone 的横坐标和纵坐标在并查集中进行合并。
        0 <= xi, yi <= 10^4，所以可以把横坐标全部减去 10001 或者全部加上 10001，或者按位取反（[0, 10000] 里的 32 位整数，最高位变成 1以后，一定不在 [0, 10000] 里）。

        时间复杂度：O(nlogA)  n是stones长度，A是不重复的横坐标和纵坐标数字之和。
        空间复杂度：O(A)  底层字典的长度A
        '''
        uf = UnionFind()
        for stone1, stone2 in stones:
            uf.union(stone1 + 10001, stone2)
        return len(stones) - uf.getCount()

class UnionFind:
    def __init__(self):
        '''
        定义可扩展的父节点字典，以及图的连通数量
        '''
        self.parent = {}
        self.count = 0

    def getCount(self):
        '''
        并查集里我们需要维护连通分量的个数，新创建顶点的时候连通分量加 11；合并不在同一个连通分量中的两个并查集的时候，连通分量减 11。
        '''
        return self.count

    def find(self, x):
        '''
        如果一个要查找的结点不在parent字典中，则count加一
        '''
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        '''
        如果两个根节点不同的点，要进行合并，则count减一
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
            
        self.parent[root_x] = self.parent[root_y]
        self.count -= 1
# @lc code=end

