#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找，mid^2 = x 
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
        
        '''
        # 牛顿迭代法
        r = x
        while r * r > x:
            r = (r + x/r) // 2
        return int(r)
        '''
# @lc code=end

