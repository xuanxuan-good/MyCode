#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 1.头指针，一个++，一个--  2.浅拷贝(复制外层的容器不会随之改变)
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        '''
        s[:] = s[::-1]
        '''
# @lc code=end

