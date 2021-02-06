#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        # O(nlogn)
        if len(nums) < 2:
            return 0
        nums.sort()
        maximum = 0
        for i in range(1, len(nums)):
            maximum = max(maximum, nums[i]-nums[i-1])
        return maximum
        '''
        # 桶排序 O(n)
        if len(nums) < 2 or min(nums) == max(nums):  # 优化
            return 0
        a, b = min(nums), max(nums)
        size = math.ceil((b-a)/(len(nums)-1))
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in nums:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))
# @lc code=end

