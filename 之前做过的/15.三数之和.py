#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1.三层暴力枚举 O(n^3)
        # 2.两层暴力+hash O(n^2) 空间复杂度O(n)
        # 3.a+b=-c,双指针，夹逼√
        nums.sort()
        results = []
        for first in range(len(nums)-2):  #!!!
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # target = -nums[first]
            second, third = first+1, len(nums)-1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum < 0:
                    second += 1
                elif sum > 0:
                    third -= 1
                else:
                    results.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    second += 1
                    third -= 1
        return results
        '''
        if len(nums)<3:
            return []
        nums.sort()
        # print(nums)
        results = []
        for first in range(len(nums)-2):  #!!!
            if first>0 and nums[first]==nums[first-1]:
                continue
            target = -nums[first]
            third = len(nums)-1
            for second in range(first+1,len(nums)-1):
                if second>first+1 and nums[second]==nums[second-1]:
                    continue
                while second < third and nums[second]+nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second]+nums[third] == target:
                    results.append([nums[first], nums[second], nums[third]])
        return results
        '''
# @lc code=end

