#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] >= A[i+1] for i in range(len(A)-1)) or all(A[i] <= A[i+1] for i in range(len(A)-1))
        '''
        if A[0] > A[-1]:
            A = A[::-1]
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return False
        return True
        '''
# @lc code=end

