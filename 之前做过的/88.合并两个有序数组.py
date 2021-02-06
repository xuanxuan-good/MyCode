#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 3.双指针 从后向前  O(m+n) 空O(1)  只要2的放进去了 就都排好了  32ms 96%
        # p1 = m-1; p2 = n-1; p = m+n-1
        # while p1 >= 0 and p2 >= 0:
        #     if nums1[p1] > nums2[p2]:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     p -= 1
        # nums1[:p2+1] = nums2[:p2+1]
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        '''
        # 2.双指针，从前向后O(m+n) 空O(n)  40ms 73%
        nums1_copy = nums1[:m]
        # print(nums1_copy)
        nums1[:] = []
        # print(nums1)
        p1 = 0; p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] > nums2[p2]:
                nums1.append(nums2[p2])
                p2 += 1
            else:
                nums1.append(nums1_copy[p1])
                p1 += 1
        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]
        '''

        '''
        #1.合并后排序  O((m+n)log(m+n))  44ms 48%
        for inde, num2 in enumerate(nums2):
            nums1[m+inde] = num2
        nums1.sort()
        '''
# @lc code=end

