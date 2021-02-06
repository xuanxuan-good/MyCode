#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1.hashmap
        # 2.sort，双指针
        # 3.collections库
        a = collections.Counter(nums1) & collections.Counter(nums2)  #48ms 99%
        # print(a.elements())
        # print(list(a.elements()))
        return list(a.elements())
        '''
        nums1.sort()  #60ms 79%
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
        '''

        '''
        if len(nums1) > len(nums2):  #56ms 91%
            return self.intersect(nums2, nums1)
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        # print(m)
        res = []
        for i in nums2:
            if (count := m.get(i, 0)) > 0:
                res.append(i)
                m[i] -= 1
        return res
        '''
# @lc code=end

