#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

# 示例：
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 注意到任意两个点之间只有唯一一条路径互相到达。

# 示例 3：
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4

# 示例 4：
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000

# 示例 5：
# 输入：points = [[0,0]]
# 输出：0
 

# 提示：
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# 所有点 (xi, yi) 两两不同。

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim算法 堆优化  O(NlogN)  O(N)
        manhattan = lambda x, y: (abs(x[0]-y[0]) + abs(x[1]-y[1]))
        
        ans, n = 0, len(points)
        visited = set()
        # Prim算法步骤一：select a random point as the starting point u
        vertices = [(0, (0, 0))]
        
        # Prim算法步骤四：将步骤2和3重复n-1次，直到所有接结点都加入到树中
        while len(visited) < n:
            # Prim算法步骤二：在“未加入树中的节点v”中遍历，找到和树距离最小的节点，加入树
            w, (u, v) = heapq.heappop(vertices)            
            if v in visited: continue  # 这样做可以使代码宽度更短
            ans += w
            visited.add(v)
            # Prim算法步骤三：更新“未加入树中的节点”到树的最小距离
            for j in range(n):
                if j not in visited:
                    heapq.heappush(vertices, (manhattan(points[j], points[v]), (v, j)))
        return ans
        
# @lc code=end

'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim算法 O(N^2)  O(N)  以顶点为单位，与图中边数无关，适合于稠密图。
        n = len(points)
        if len(points) == 1: return 0
        res = 0
        # Prim算法步骤一：select a random point as the starting point
        curr = 0 
        dis = [math.inf] * n
        visited = set()
        
        # Prim算法步骤四：将步骤2和3重复n-1次，直到所有接结点都加入到树中
        for i in range(n - 1):
            x0, y0 = points[curr]
            visited.add(curr)
            # Prim算法步骤二：在“未加入树中的节点”中遍历，找到和树距离最小的节点，加入树
            for j, (x, y) in enumerate(points):
                if j not in visited:
                    dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
            # Prim算法步骤三：更新“未加入树中的节点”到树的最小距离
            delta, curr = min((d, j) for j, d in enumerate(dis)) 
            dis[curr] = math.inf
            res += delta
            
        return res
'''


'''
class UnionFind:
    def __init__(self, n):
        '''
        # 并查集，查找，合并（按结点数量）
        '''
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        '''
        # 按结点数量合并
        # 如果边的两点连接的是不同的连通分量，返回true，(说明图中加入这条边不会形成环，即只有一条简单路径)
        '''
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        self.size[rootX] += self.size[rootY]
        self.parent[rootX] = rootY
        return True
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        # 最小生成树 Kruskal 算法 以边为单位，时间取决于边数，适合于稀疏图
        # 能够满足‘任意两点之间有且仅有一条简单路径’只有树，且这棵树包含 n 个节点。称这棵树为给定的图的生成树，其中‘总权值最小’的生成树，称其为最小生成树。
        # 时间复杂度：O(n^2logn)，其中 n 是节点数。一般 Kruskal 是 O(mlogm) 的算法，但本题中 m=n^2
        # 空间复杂度：O(n^2)，其中 n 是节点数。并查集使用 O(n) 的空间，edges数组需要使用 O(n^2)的空间。
        # 2.可以想办法降低边数--树状数组
        '''
        # 曼哈顿距离  用索引表示
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        n = len(points)
        uf = UnionFind(n)
        edges = []
        # Kruskal 算法步骤一：将图G{V,E}中所有边从小到大按距离排序,相等的按任意顺序
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        edges.sort()

        # Kruskal 算法步骤二：初始化G',从前向后扫描排序后的边，如果边在G‘中连接了两个相异的连通块，则将它插入G'中
        ret, num = 0, 1
        for length, x, y in edges:
            if uf.union(x, y):
                ret += length
                num += 1
            if num == n:
                break

        return ret
'''
