#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。
# 在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

# 示例 ：
# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        并查集
        首先将所有关系为“==”的字符串方程，对应的两个值，进行合并
        之后所有关系为“！=”的字符串方程，如果两个值对应的根节点是相同的，则产生了矛盾，返回false

        时间复杂度：O(n + ClogC)
            n是equations中的方程数量，C是变量的总数，本题中是小写字母，因此C <= 26。
            使用了路径压缩，对于每个方程的合并和查找，均摊时间复杂度都是O(logC)。
            --个人理解整个程序可以认为是1，遍历一遍整个方程 2.合并或者查找整个方程，所以可以相加。（因为每次遍历都需要一半不符合的跳过，一般合并或查找）
        空间复杂度：O(C)
            创建一个数组parent存储每个变量的连通分量信息，由于变量都是小写字母，因此parent长度是C。
        '''
        self.p = list(range(26))  # 都是小写字母，所以设置为26个就可以了
        # 底层用数组实现，方便编码
        for st in equations:
            if st[1] == '=':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                self.union(index1, index2)
        for st in equations:
            if st[1] == '!':
                index1 = ord(st[0]) - ord('a')
                index2 = ord(st[3]) - ord('a')
                if self.find(index1) == self.find(index2):
                    return False
        return True
    
    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        self.p[p2] = p1

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]
# @lc code=end

