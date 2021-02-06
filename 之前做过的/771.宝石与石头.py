#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 找石头中有多少个宝石 1.暴力O(mn) 2.set遍历的时间复杂度是1 O(m) 
        jewels = set(jewels)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count
# @lc code=end

