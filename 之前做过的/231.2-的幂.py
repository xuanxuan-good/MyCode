#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 是二次幂，即这个整数表示的二进制位 有且仅有 一个二进制位是1
        # n>0 n&(n-1) == 0
        return n > 0 and n & (n-1) == 0
# @lc code=end

