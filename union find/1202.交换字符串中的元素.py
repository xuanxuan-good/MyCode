#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
# 0 <= pairs.length <= 10^5

# 示例 :
# 输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        '''
        按秩合并：以 i 为根结点的子树的高度 [又叫启发式合并]
        引入路径压缩后，虽然rank不是此时树的准确高度，但是不会出现树a的高度比树b的高度高，但树a的rank却比树b的rank低的情况
        parent每个节点的父节点
        '''
        self.rank = [1] * n
        self.parent = list(range(n))
    
    def union(self, x: int, y: int):
        '''
        如果两个结点的根结点相同，则不需要再合并了
        否则，按秩合并，底高度的指向高高度的，使树的高度不在增加
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
    
    def find(self, x: int) -> int:
        '''
        隔代压缩
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        '''
        字典序：ASCII值越小的字符位于字符串中的位置越靠前，整个字符串的字典序就越靠前
        将任意交换的结点对，输入并查集,来实现属于同一连通分量元素的合并工作
        构建映射关系，Java中可以建一个<整形，优先队列>的hashmap; key:连通分量的根结点（也叫代表元），value:同一连通分量的字符集合
        也就是把属于同一个根结点的字符放在一起，之后再对从小到大排好序的，属于同一连通分量的字符，分别放到属于同一根结点的元素的位置

        时间复杂度：O((M+N)α(N) + NlogN)
            M是数组pairs的长度，N是输入字符串s的长度，α是Ackermann的反函数。
            1.遍历数组paris需要O(M)，并查集每次合并（按秩合并）的同时路径压缩，时间复杂度O(α(N))
            2.遍历字符串s，长度N，并查集每次查询，时间复杂度O(α(N))；极端情况下，所有字符都在一个优先队列里。总时间复杂度O(N(α(N) + logN))--先查询，在调整堆，有时间先后顺序，所以相加
            3.极端情况下，所有字符都在一个优先队列里，并查集每次查询，时间复杂度O(α(N))；每一次调整堆选出最小的字符，时间复杂度为O(logN)，一共N次调整堆；总时间复杂度O(N(α(N) + logN))
        空间复杂度：O(N)
            并查集长度N，字典长度N，所有优先队列中加起来一共N个字符，保存结果需要N个字符。
        '''
        if len(pairs) == 0:
            return s
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)
        
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            heapq.heappush(mp[uf.find(i)], ch)  # 把相同根节点的字符，heappush在同一个字典的key下边
        
        res = ""
        for i in range(len(s)):
            res += heapq.heappop(mp[uf.find(i)])
        return res
        
# @lc code=end

