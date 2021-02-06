#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:  # 
            return False
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right-left) // 2
            row = mid // n; col = mid % n  # relation
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

