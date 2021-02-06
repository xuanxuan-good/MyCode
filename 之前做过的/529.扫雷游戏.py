#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1,-1), (1, 1), (1, -1))
        if board[row][col] == 'M':
            board[row][col] = 'X'
        elif board[row][col] == 'E':
            n = sum([board[row+r][col+c] == 'M' for r, c in directions if 0 <= row+r < len(board) and 0 <= col+c < len(board[0])])
            board[row][col] = str(n or 'B')
            for i, j in directions * (not n):
                if 0 <= row+i < len(board) and 0 <= col+j < len(board[0]):
                    self.updateBoard(board, (row+i, col+j))
        return board
# @lc code=end

