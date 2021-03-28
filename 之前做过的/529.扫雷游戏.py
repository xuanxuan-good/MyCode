#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
# 给定一个代表游戏板的二维字符矩阵。 
# 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
# 数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
# 现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

# 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
# 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
# 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
# 如果在此次点击中，若无更多方块可被揭露，则返回面板。

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

