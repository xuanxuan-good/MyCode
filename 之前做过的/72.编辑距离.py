#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    @functools.lru_cache()
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        # 1.递归+记忆化 自顶向下 初始 0 0
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) or len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            w1 = self.minDistance(word1[1:], word2[1:])
            w2 = self.minDistance(word1, word2[1:])
            w3 = self.minDistance(word1[1:], word2)
            return 1 + min(w1, w2, w3)
        '''
        
        # 2.动态规划 O(mn) O(mn) 自底向上 插入替换 删除 dp[i][j]表示word1的i位置，转到word2的j位置 需要的最少步数
            # w1 = "", w2 = ""; w1 = "", w2 = "..."; w1 = ...d(i), w2 = ...(j)
            # 初始化：dp[0][j]=j, dp[i][0]=i
            # dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j]  else:
            # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

