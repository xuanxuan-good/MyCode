#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in hashtable:
                return [hashtable[t], i]
            hashtable[nums[i]] = i
        return [-1, -1]
# @lc code=end