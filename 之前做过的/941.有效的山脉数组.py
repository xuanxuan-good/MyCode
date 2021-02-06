#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # 2.双指针
        n = len(A)
        left, right = 0, n-1
        while left < n-1 and A[left] < A[left+1]:
            left += 1
        while right > 0 and A[right-1] > A[right]:
            right -= 1
        return 0 < left == right < n-1
        '''
        # 1.单指针
        i, n = 0, len(A)
        while i < n-1 and A[i] < A[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        while i < n-1 and A[i] > A[i+1]:
            i += 1
        return i == n-1
        '''
# @lc code=end

