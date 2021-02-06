#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        计算s的子序列在t中出现的次数，s = "rabbbit", t = "rabbit"
        dp[i][j]表示，s的前j个字符中，t的前i个字符出现的次数（字符串下标为i-1,j-1）
        初始化：dp[0][j]=1
        状态方程：dp[i][j] = dp[i-1][j-1] + dp[i][j-1] if t[i-1]==s[j-1]
                else: dp[i][j] = dp[i][j-1]
        '''
        m, n = len(t), len(s)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):  # dp[0][0] == 1
            dp[0][j] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

