**最小生成树**：能够满足‘任意两点之间有且仅有一条简单路径’只有树，且这棵树包含 n 个节点。称这棵树为给定的图的生成树，其中‘总权值最小’的生成树，称其为最小生成树。

最小生成树的**两种算法**：

**Kruskal 算法：**

以边为单位，时间取决于边数，适合于稀疏图。

① Kruskal 算法步骤一：将图G{V,E}中所有边从小到大按距离排序,相等的按任意顺序。

② Kruskal 算法步骤二：初始化G',从前向后扫描排序后的边，如果边在G‘中连接了两个相异的连通块，则将它插入G'中。

③ Kruskal 算法步骤三：最后的G'就是G的最小生成树。

Kruskal 算法的优化：

树状数组

**Prim算法：**

以顶点为单位，与图中边数无关，适合于稠密图。

Prim算法步骤一：select a random point as the starting point u。

Prim算法步骤二：在“未加入树中的节点v”中遍历，找到和树距离最小的节点，加入树。

Prim算法步骤三：更新“未加入树中的节点”到树的最小距离。

Prim算法步骤四：将步骤2和3重复n-1次，直到所有接结点都加入到树中。

**Prim算法的堆优化：**

Prim算法在找最小距离时，可以不用所有结点都遍历一遍，可以将所有结点存放到一个最小堆里，查找最小的时间复杂度就从 n 变成了 logn 。

```python
例题：1584.连接所有点的最小费用（最小生成树：Kruskal算法；Prim算法）
     1489.找到最小生成树里的关键边和伪关键边(最小生成树：Kruskal算法)
```
