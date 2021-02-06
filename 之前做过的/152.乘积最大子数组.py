#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 两个负数相乘 有可能是正数(因此最大值可能变成最小值，反之亦可能)；有零时需要重置 dp
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n*big, n*small, n), min(n*big, n*small, n)
            maximum = max(maximum, big)
        return maximum
# @lc code=end

