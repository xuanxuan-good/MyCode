#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countAB = collections.Counter(a+b for a in A for b in B)
        # print(countAB)
        res = 0
        for u in C:
            for v in D:
                if countAB[-u-v] > 0:
                    res += countAB[-u-v]
        return res
# @lc code=end

