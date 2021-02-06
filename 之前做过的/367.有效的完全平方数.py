#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # mid^2 mid>1 -> 抛物线右侧单调递增
        if num == 0 or num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = left + (right-left) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

