#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # dfs
        res = []
        self.dfs(nums, res, [])
        return res
    def dfs(self, nums, res, tmp):
        if len(tmp) > 1:
            res.append(tmp)
        visited = set()
        for inx, i in enumerate(nums):
            if i in visited:
                continue
            if not tmp or i >= tmp[-1]:
                visited.add(i)
                self.dfs(nums[inx+1:], res, tmp + [i])
# @lc code=end

