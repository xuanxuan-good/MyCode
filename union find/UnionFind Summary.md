并查集支持两种操作：合并（union--把两个不相交的集合合并为一个集合）和查询（find--查询两个元素是否在同一个集合中）。

并查集的特色：边查询边修改。

有几种处理方式：union：按秩合并；find的路径压缩：完全压缩，隔代压缩

```python
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
```python
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
关于399.除法求值的权重计算问题。

1.四边形法则求权重：

![图片](https://uploader.shimo.im/f/hRhpbx3ZMOeYGZvK.png!thumbnail?fileGuid=8PiaO2yrHgIIimzI)

2.隔代路径压缩的权重变化： 是一个递归的隔代压缩过程，递归到最里层，逐层乘原始权重，就得到当前节点权重。

![图片](https://uploader.shimo.im/f/n2VuA2TfDBbBQV99.png!thumbnail?fileGuid=8PiaO2yrHgIIimzI)

```
# 关于399.除法求值：
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

空间复杂度分析：一般为并查集初始化时，几个变量的长度。

