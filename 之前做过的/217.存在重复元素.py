#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1.排序，之后看相邻元素有相同的就true
        # 2.哈希，之后遍历的元素在hash中出现就true
        # 3.collections
        '''
        if not nums:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
        '''

        '''
        hashtable = set()
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return True
            hashtable.add(nums[i])
        return False
        '''

        if not nums:
            return False
        res = collections.Counter(nums)
        if res.most_common(1)[0][1] >= 2:
            return True
        return False
# @lc code=end

