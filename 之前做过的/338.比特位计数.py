#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0
            while i != 0:
                i = i & (i-1)
                count += 1
            res.append(count)
        return res
        
        '''
        # 布莱恩尼克根算法  dp+位运算
        dp = [0] * (num+1)
        for i in range(1, num+1):
            dp[i] = dp[i&(i-1)] + 1
        return dp
        '''
# @lc code=end

