#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.loop,count zero,
        # 2.new array,loop
        # 3.array-index √
        
        '''
        #array-index  40ms 85%
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i!=j:
                    nums[i] = 0
                j += 1  #!!!location
        '''
        '''
        #exchange
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        '''
        '''
        # count zero
        snowballs = 0
        for i in range(len(nums)):
            if nums[i]==0:
                snowballs += 1
            elif snowballs>0:
                nums[i-snowballs] = nums[i]
                nums[i] = 0
        '''
# @lc code=end

