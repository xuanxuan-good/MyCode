#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 栈O(n) O(n) 存索引  当前遍历到的矩形的下标 与 出栈后的矩形的下标 之差 - 1 = 矩形宽度
        '''
              1
            1 1
            1 1
            1 1
        1   1 1 1
        1 1 1 1 1
          √     √
        '''

        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return maxarea

        '''
        # 暴力O(n^2) O(1) 枚举每个柱形为高度的最大柱形的面积--依次遍历柱形的高度，每个高度分别向两边扩散，求以当前高度为矩形的最大宽度
        # 即左右两边分别找到不大于等于当前柱形高度的边界值
        n = len(heights)
        res = 0
        for i in range(n):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left-1] >= cur_height:
                left -= 1
            right = i
            while right < n-1 and heights[right+1] >= cur_height:
                right += 1
            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res
# @lc code=end

