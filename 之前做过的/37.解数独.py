#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # A*?
        # 每个位置可以放置1-9，要看放置的数 行列及小格子是否重复
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i//3)*3 + j//3].remove(val)
                else:
                    empty.append((i, j))
    
        def backtrack(iter = 0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i//3)*3 + j//3
            # print(row[i], col[j], block[b], row[i] & col[j] & block[b])  # {4, 6} {1, 2, 3, 4, 5, 9} {1, 2, 3, 4, 5, 7, 8} {4}交集
            for val in row[i] & col[j] & block[b]:  # & 求三个set的交集
                row[i].remove(val)  # 尝试填充，如果发现重复了，那么擦除重新进行新一轮的尝试，直到把整个数组填充完成。
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯  当前格子不能填任何一个数字就回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()
# @lc code=end

