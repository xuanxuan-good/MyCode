#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 写循环判断，看行和列，是否这些数字只出现一次
        seen = []
        for i, row in enumerate(board):  # 读多行
            # print(i)  # 0-8
            for j, c in enumerate(row):  # 针对每一行
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]  # 字符数和数用相反的顺序区分开了
        return len(seen) == len(set(seen))
# @lc code=end

