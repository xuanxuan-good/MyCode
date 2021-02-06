#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # ...15,相当于5之前的编码方法数与15之前的编码方法数 之和 就是总的编码方法数
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1
        # 15 dp[2] = dp[1]+dp[0] --- 1,5;15---1+1=2  dp[0]=1
        for i in range(2, len(s)+1):
            if int(s[i-1]) > 0:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
# @lc code=end

