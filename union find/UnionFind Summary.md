并查集支持两种操作：合并（union--把两个不相交的集合合并为一个集合）和查询（find--查询元素的根节点）。

并查集的特色：边查询边修改。

有几种处理方式：union：按秩合并（分为按树的高度合并，按结点数量合并）；find：路径压缩（分为完全压缩，隔代压缩）

能用并查集来做的题目，应该都是可以用深搜，宽搜来做的，具体如何做。。。

**并查集模板一：（完全压缩）**

```python
例题：547.朋友圈（省份数量）
class UnionFind:
    def __init__(self, n):
        p = list(range(n))  # 并查集初始化
    def union(self, p, i, j):
        p1 = self.find(p, i)
        p2 = self.find(p, j)
        p[p2] = p1
    def find(self, p, i):
        '''
        完全压缩
        '''
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 完全压缩，每个不直接与根节点相连的结点，直接与根节点相连。
            x = i; i = p[i]; p[x] = root
        return root
```
**并查集模板二：（按树的高度合并+隔代压缩）**

```python
隔代压缩例题：684.冗余连接 721.账户合并 990.等式方程的可满足性
按树的高度合并例题：1202.交换字符串中的元素
class UnionFind:
    def __init__(self, n):
        # 引入路径压缩后，虽然rank不是此时树的准确高度，但是不会出现树a的高度比树b的高度高，但树a的rank却比树b的rank低的情况
        self.parent = list(range(n))  # parent每个节点的父节点
        self.rank = [1] * n  # 按秩合并：以 i 为根结点的子树的高度 [又叫启发式合并]
    def union(self, x, y):
        '''
        如果两个结点的根结点相同，则不需要再合并了
        否则，按秩合并，底高度的指向高高度的，使树的高度不再增加
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
             return
        if self.rank[root_x] == self.rank[root_y]:
            self.parent[root_x] = root_y
            # 以 rootY 为根结点的树，高度增加一
            self.rank[root_y] += 1
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            # 以root_y为根结点的树的高度不变
        else:
            # 以root_x为根结点的树的高度不变
            self.parent[root_y] = root_x
    def find(self, x):
        '''
	    隔代压缩
	    '''
	    if self.parent[x] != x:
	        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```
**并查集模板三：（按结点数量合并+隔代压缩+setCount连通量个数计算）**

```python
例题：1489.找到最小生成树里的关键边和伪关键边(最小生成树：Kruskal算法)
按结点数量合并例题：1584.连接所有点的最小费用（最小生成树：Kruskal算法；Prim算法）
计算结点数量例题：1319.连通网络的操作次数
困难题：803.打砖块（按结点数量合并，计算根节点下结点数量）
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        # 按结点个数合并，将结点数量少的根节点指向 多的根节点，使得少的一端结点数量不增加
        self.size = [1] * n  
        # 计算连通分量个数，每次合并时，把连通分量数目减一
        self.setCount = n  
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.setCount -= 1
```
**并查集模板四：（可扩展父节点字典+隔代压缩+getCount计算连通量个数）**

当数值范围很大，但是实际用到的数不是很多的时候，可以考虑底层用可扩展的字典。没必要用数组存储全部的无意义数。

```python
例题：947.移除最多的同行或同列石头
class UnionFind:
    def __init__(self):
        '''
        定义可扩展的父节点字典，以及图的连通数量
        '''
        self.parent = {}
        self.count = 0
    def getCount(self):
        '''
        并查集里我们需要维护连通分量的个数，新创建顶点的时候连通分量加 11；合并不在同一个连通分量中的两个并查集的时候，连通分量减 11。
        '''
        return self.count
    def find(self, x):
        '''
        如果一个要查找的结点不在parent字典中，则count加一
        '''
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        '''
        如果两个根节点不同的点，要进行合并，则count减一
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
            
        self.parent[root_x] = root_y
        self.count -= 1
```
关于**399.除法求值**的权重计算问题。

（隔代压缩，**权重计算**，**isConnected函数返回除法结果**）

1.四边形法则求权重：

![图片](https://uploader.shimo.im/f/hRhpbx3ZMOeYGZvK.png!thumbnail?fileGuid=8PiaO2yrHgIIimzI)

2.隔代路径压缩的权重变化： 是一个递归的隔代压缩过程，递归到最里层，逐层乘原始权重，就得到当前节点权重。

![图片](https://uploader.shimo.im/f/n2VuA2TfDBbBQV99.png!thumbnail?fileGuid=8PiaO2yrHgIIimzI)

```
# 399.除法求值：
class UnionFind:
	    def __init__(self, n):
	        """
	        记录每个节点的父节点，值分别是1~n
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
	        路径压缩（隔代压缩）记录x -> parent[x]为origin，一层一层最后找到x的根节点为parent[x]
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
```
时间复杂度分析：每一次合并或查询的均摊时间复杂度为O(logn)。具体的题还要根据具体的程序判断总的复杂度（有时间上先后顺序的相加处理）。

空间复杂度分析：一般为并查集初始化时，变量的长度。

