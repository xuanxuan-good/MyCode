#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 位运算
        ？
        '''
        # dfs
        def dfs(queens, xy_diff, xy_sum):  # 三个判重的数组，列，撇，捺，被攻击的范围
            p = len(queens)
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
        res = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]
        '''
# @lc code=end

