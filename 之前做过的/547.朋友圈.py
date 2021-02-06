#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        #   2.并查集
        if not M:
            return 0
        n = len(M)
        p = [i for i in range(n)]  # 并查集初始化

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(p, i, j)  # 遍历矩阵M，如果有1就进行合并
        return len(set([self.parent(p, i) for i in range(n)]))  # 遍历所有结点，看所有结点里 不同parent有多少个
    
    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p2] = p1
        # p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # i 压缩路径
            x = i; i = p[i]; p[x] = root
        return root

        '''
        #  2.BFS  O(n^2) O(n)
        visited = [0] * len(M)
        count = 0
        queue = []
        for i in range(len(M)):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    s = queue.pop()
                    visited[s] = 1
                    for j in range(len(M)):
                        if M[s][j] == 1 and visited[j] == 0:
                            queue.append(j)
                count += 1
        return count
        '''

        '''
        # 1.dfs  类似 岛屿问题 O(n^2) O(n)
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1  # ！！！
                self.dfs(M, visited, j)
    '''
# @lc code=end

