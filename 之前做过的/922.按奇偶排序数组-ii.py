#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        res = []
        for j in range(len(A)//2):
            res.append(even[j])
            res.append(odd[j])
        return res
# @lc code=end

