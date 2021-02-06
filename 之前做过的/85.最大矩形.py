 #
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        1.暴力：枚举每个可能的矩形（x1,y1）->(x2,y2),O(N^2M^2),再遍历两个点为对角顶点的矩形O(MN)
        √2.DP-柱形图优化暴力O(N M^2) O(N M)：记录每一行中每个方块连续1的个数，每遍历一行，更新该点的最大可能宽度
            row[i] = row[i-1] + 1 if row[i] == '1'   遍历列时，每个宽度的最小值
            实际上就是将输入转化成一系列柱状图，每一栏O(N)是一个新的柱状图。针对每个柱状图计算最大面积。
        √3.柱状图-栈O(N M) O(M),应用84题--柱状图中最大柱形
        4.dp-每个点的最大高度O(N M) O(M)，对每个点，计算矩形的高h，左边界l和右边界r--问题转化为更新每个数组
            new_height[j] = old_height[j] + 1 if row[j] == '1' else 0
            new_left[j] = max(old_left[j], cur_left)
            new_right[j] = min(old_right[j], cur_right)
        '''

        if not matrix:
            return 0
        maxarea = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1  # 记录的是每个位置左侧连续1的个数
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea

        '''
        if not matrix:
            return 0
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0  # 记录的是每个位置上方连续1的个数
            maxarea = max(maxarea, self.largestRectangleArea(dp))  # 针对每一个列，缩进位置！！！
        return maxarea

    def largestRectangleArea(self, heights):
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

        '''
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea
        '''

# @lc code=end

