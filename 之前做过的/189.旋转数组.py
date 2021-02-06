#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.暴力，O(n*k) : loop 1->k pre=nums[n-1] 
        #                       loop j 1->n temp=nums[j];nums[j]=pre;pre=temp
        # 2.额外数组 O(n) O(n) : loop i 0->length a[(i+k)%n] = nums[i]
        # 3.使用环状替换 O(n) ???看不懂
        # 4.使用反转 O(n) O(1) 
        '''
        k = k % len(nums)
        if not k:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        '''
        k = k % len(nums)
        self._reverse(nums, 0, len(nums)-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, len(nums)-1)
    def _reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1; end -= 1
# @lc code=end

