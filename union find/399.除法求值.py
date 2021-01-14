#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#'[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
# 每个 Ai 或 Bi 是一个表示单个变量的字符串。

# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

# 示例
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

# @lc code=start
class UnionFind:
    def __init__(self, n):
        """
        记录每个节点的父节点，值分别是1-n
        记录每个节点到根节点的权重，初始权重为1
        """
        self.parent = list(range(n))
        self.weight = [1] * n
        
    def union(self, x, y, value):  # java double value
        """
        合并两个节点xy，如果两个结点的根节点相同，则已经是合并好的
        如果不同，则进行节点合并和权重计算
        """
        root_x,root_y = self.find(x),self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y  # root_x指向root_y
        ##### 四边形法则更新根节点的权重: 
        # x --> root_x [weightx]  y --> root_y [weighty]  x --> y [value]  求的是root_x --> root_y
        self.weight[root_x] = self.weight[y] * value / self.weight[x]
    
    def find(self, x):
        """
        查找x的根节点，如果x的父节点不是自己，则要“一边寻找一边修改结点指向”[这是并查集的特点]
        路径压缩（隔代压缩？）记录x -> parent[x]为origin，一层一层最后找到x的根节点为parent[x]
        更新权重 x结点的权重只要一直*=之前origin的权重即可
        """
        if x != self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])  # 递归，找x的根节点
            self.weight[x] *= self.weight[origin]
        return self.parent[x]  # 根节点

    def isConnected(self, x, y):
        """
        两节点是否相连
        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return self.weight[x] / self.weight[y]  # 2.同一个根节点下，可以直接计算得到权值
        else:
            return -1.0  # 3.可能会出现根节点不同的情况，可能是形成了不同的集合
            

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        时间复杂度：O((N + Q) logA)
            构建并查集 O(NlogA) N为equationsSize，每执行一次合并操作的时间复杂度是O(logA)，A是equations里'不同字符'的个数
            查询并查集 O(QlogA) Q为len(queries)，每一次查询时执行路径压缩的时间复杂度是O(logA)--个人理解时树的高度
        空间复杂度：O(A)
            创建字符与ids对应关系dicts长度为A，并查集底层使用的两个数组parent和weight存储每个变量的连通分量信息，parent和weight的长度均为A
        '''
        equationsSize = len(equations)
        uf = UnionFind(2 * equationsSize)   # 这个大小，是最多情况下，所有字符都不同
        # 底层用数组实现，方便编码
        ids, dicts = 0, {}
        for (a, b), value in zip(equations, values):
            if a not in dicts:
                dicts[a] = ids
                ids += 1
            if b not in dicts:
                dicts[b] = ids
                ids += 1
            uf.union(dicts[a], dicts[b], value)
    
        res = [0] * len(queries)

        for i, (a, b) in enumerate(queries):
            if a not in dicts or b not in dicts:  # 1.这个字符不在已知条件中出现
                res[i] = -1.0
            else:
                res[i] = uf.isConnected(dicts[a], dicts[b])
            
        return res

# @lc code=end

