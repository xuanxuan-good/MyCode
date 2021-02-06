#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        m = collections.Counter(nums2)
        for i in nums1:
            if m.get(i, 0) > 0:
                res.append(i)
                m.pop(i)
        return res
        
        '''
        # 排序 双指针
        nums1.sort()
        nums2.sort()  #!!!
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):  #!!!
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return set(res)
        '''

        '''
        a = collections.Counter(nums1) & collections.Counter(nums2)
        b = list(a.elements())
        return set(b)
        '''
# @lc code=end

