#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 所有的不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上
    #    把边界 O 并且与它连通这些点分在一起
        # 并查集 代码学习
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])  # find(f[x])
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)

            
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col  #
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":  # 等于O并且在边界上，就和dummy合并；不在边界上 就向四个方向上有O的合并
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)  # 为什么要和dummy union  相当于哨兵？
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 如果不在边界就遍历四个方向
                            if board[i + x][j + y] == "O":  #!!!
                                union(i * col + j, (i + x) * col + (j + y))  # 为0就要继续合并
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        '''
        # dfs    # product同时进入多个循环
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != 'O':
                return
            board[i][j] = '.'
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i+r, j+c)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i, j in product(range(m), range(n)):
            board[i][j] = 'O' if board[i][j] == '.' else 'X'
        '''

        '''
        # bfs
        if not board:
            return
        
        n, m = len(board), len(board[0])
        que = collections.deque()  # 双端队列；四个边界为O的 位置 加入到que中
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
        
        while que:
            x, y = que.popleft()
            board[x][y] = "A"  # 每个位置赋值为A，同时遍历四个方向，
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))  # 周围有相邻的O则继续加入到que中
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        '''
# @lc code=end

