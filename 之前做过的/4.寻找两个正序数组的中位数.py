#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)  # 总长度
        if n % 2 == 1:  # 奇数
            return self.findKth(nums1, 0, nums2, 0, n // 2 + 1)  # k表示位置
        else:  # 偶数
            smaller = self.findKth(nums1, 0, nums2, 0, n // 2)
            bigger = self.findKth(nums1, 0, nums2, 0, n // 2 + 1)
            return (smaller + bigger) / 2
    def findKth(self, A, index_a, B, index_b, k):
        if len(A) == index_a:  # 只有B
            return B[index_b + k - 1]  # 索引位置
        if len(B) == index_b:  # 只有A
            return A[index_a + k - 1]
        if k == 1:
            return min(A[index_a], B[index_b])  # 只有一个元素，返回首元素最小值
        
        a = A[index_a + k // 2 - 1] if index_a + k // 2 <= len(A) else None
        b = B[index_b + k // 2 - 1] if index_b + k // 2 <= len(B) else None  # 元素位置 小于 数组长度，再去相应位置的值

        if b is None or(a is not None and a < b):
            return self.findKth(A, index_a + k // 2, B, index_b, k - k // 2)
            # a小并且a不空，则去除a左侧部分；或者b为空
        return self.findKth(A, index_a, B, index_b + k // 2, k - k // 2)
# @lc code=end

