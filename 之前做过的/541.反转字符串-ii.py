#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # python中字符串是不可变的,所以需要转换为列表再reverse
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
        
        '''
        # recursion
        if len(s) < k:
            return s[::-1]
        if len(s) < 2*k:
            return s[:k][::-1] + s[k:]
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k)
        '''
# @lc code=end

