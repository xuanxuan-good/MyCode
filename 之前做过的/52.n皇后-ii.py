#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 位运算--代码学习
        if n < 1:
            return []
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count
    def dfs(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 拿可以放的位置
        # print(bits)      # 1111√;1100√;0000√(count=0);0010;0000;1000;0001;0100;0001;1000;0010;0011;0100;0000;0000
        while bits:
            p = bits & -bits  # 得到最低位的1 [根据最低位的一来判断列，撇，捺的位置]
            # print(bin(-bits))  # 
            # print(p)          # 0001√;0100√;1000√;0010√;0010√;1000√;0001√;0100√;0100√;0001√;1000√;0010;1000;0001;0100;0010
            bits = bits & (bits - 1)  # 清零最低位的1 [表示该位置放入皇后]
            # print(bin(bits-1))
            # print(bits, row)    # 1110√;1000√;0000√;0000√;1100√;0000√;0000√;0000√;1000√;0000√;0000√;0000;0000√;0010;0000;0000
                                             # 0000（最内侧dfs的bits=0000，返回上一层bits不为零，继续循环）
            self.dfs(n, row+1, cols | p, (pie | p) << 1, (na | p) >> 1)
s = Solution()
s.totalNQueens(4)
# @lc code=end

    '''
    # n表示递归有n层（n皇后问题） ； row表示当前在审查哪一层
    # 用三个int，int的二进制位（不超多32位即可）表示相应的列撇捺的位置是否被占据
    # 行 >= n，表示已经得到结果了
    # 三个或在一起表示所有皇后所打掉的格子，再取反，表示 没有被占的格子赋为1了；
    # & ((1 << n) — 1) 相当于把高位 n皇后的n之前的那些位 全部赋0，因为不会用到前边的位置
    # bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位；如果是8皇后，最初始就是8个二进制的1
    while bits:  # 8个1分别循环，看能放在哪一列
        p = bits & —bits # 取到最低位的1（因为-bit是加一取反）
        bits = bits & (bits — 1) # 表示在p位置上放入皇后（最低位被占据，变为0）
        self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)  # n, row+1 新的一层递归下探，撇是p所在的位置左移一位（左下）；捺是p所在位置右移一位 
        # 不需要revert  cols, pie, na 的状态
    '''