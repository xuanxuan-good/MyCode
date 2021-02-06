#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    @functools.lru_cache(None)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        # 递归 自顶向下  42/43 --加None后通过？
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            return self.longestCommonSubsequence(text1[1:], text2[1:]) + 1
        else:
            return max(self.longestCommonSubsequence(text1, text2[1:]), self.longestCommonSubsequence(text1[1:], text2))
        '''
        
        # 动态规划 O(mn) O(mn) 自底向上 初始化 0
            # 状态方程 dp[i][i] = dp[i-1][j-1] + 1 if text1[i] == text2[j]
            # else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

