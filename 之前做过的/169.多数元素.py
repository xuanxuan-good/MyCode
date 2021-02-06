#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1.暴力枚举，遍历一遍数组，针对每个数再遍历一遍数组计算次数，O(n^2)
        # 2.hash O(n) O(n) 
        # 3.排序，假设多数元素肯定存在 O(log n)
        # 4.随机，有一半以上的出现次数才是多数元素 期望时间复杂度 O(n)
        # 5.摩尔投票法 O(n) 众数+1，其他-1.则count>0表示是众数
        # 6.分治，O(nlogn) O(logn)

        # 分治 144ms 5%
        def majority_element_rec(l, h):
            # terminator
            if l == h:
                return nums[l]  # 最后数组里只有一个元素
            # current logic
            mid = (h-l) // 2 + l
            # drill down
            left = majority_element_rec(l, mid)  # 分别在左半部分和右半部分进行递归
            right = majority_element_rec(mid+1, h)
            if left == right:
                return left  # 如果两部分的多数元素是同一个值，则返回这个值
            # merge
            left_common = sum(1 for i in range(l, h+1) if nums[i] == left)
            right_common = sum(1 for i in range(l, h+1) if nums[i] == right)
            return left if left_common > right_common else right  # 如果不相同，则要计算出现次数最多的，返回
        return majority_element_rec(0, len(nums)-1)

        '''
        # 4. 摩尔投票法  52ms 65%
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate
        '''

        '''
        # 2.排序，n//2索引对应的元素就是 多数元素（多数元素肯存在的情况）O(log n) 48ms 79% 
        nums.sort()
        return nums[len(nums)//2]
        '''

        '''
        # 3.随机化,随机选值，至少有一半的几率找到众数  68ms 21%
        import random
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
        '''

        '''
        # 2.hash O(n) O(n) 
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)
        '''
# @lc code=end

