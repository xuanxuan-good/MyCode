#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        '?'表示可以匹配任何单个字符 '*'表示可以匹配任意字符串（包括空字符串）
        dp[i][j]表示p前i个字符 和 s前j个字符是否匹配，下标分别是i-1,j-1
        初始化：dp[0][0]=true 两空字符串一定匹配；
                s空，p不空，e.g. s="" p=""or"*"or"***"可匹配，一旦有一个别的字符出现"**a"，为false
        状态方程：① p[i-1]==s[j-1] 只需要知道i和j前边的子串是否匹配
                dp[i][j] = dp[i-1][j-1]
                ② p[i-1] != s[i-1] 两种情况
                    1.p[i-1] == "?" 匹配任意单个字符，本质还是① dp[i][j] = dp[i-1][j-1]
                    2.p[i-1] == "*"☆ 匹配任意字符串，可以使用或不使用
                        不使用，即匹配空串 e.g. s="abc" p="abc*" 
                            dp[i][j] = dp[i-1][j]
                        使用，e.g. s="abc" p="ab*" 让*和c匹配
                            dp[i][j] = dp[i][j-1]
        '''
        m, n = len(p), len(s)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            if p[i-1] != "*":
                break
            dp[i][0] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[j-1] == p[i-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":  # 
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

