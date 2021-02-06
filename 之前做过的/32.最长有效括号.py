#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)
# @lc code=end

