#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 想法1：在最后结果中去掉重复的项--×增加了计算量  想法2：对重复的项 提前进行剪枝
        res = []
        def dfs(nums, level):
            # terminator
            if level == len(nums):
                res.append(nums[:])
                return
            # current logic ; drill down
            visit = set()  #set()   .add
            for i in range(level, len(nums)):
                if nums[i] in visit:
                    continue
                visit.add(nums[i])
                nums[i], nums[level] = nums[level], nums[i]
                dfs(nums, level+1)
                # reverse current state
                nums[i], nums[level] = nums[level], nums[i]
        dfs(nums, 0)
        return res
# @lc code=end

